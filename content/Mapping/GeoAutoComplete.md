Title: Super flexible GeoAutoComplete with Solr
Date: 2014-02-25
Slug: Super flexible GeoAutoComplete with Solr
Author: Jérôme Bernardes
Tags: Solr,OpenSource,English
Summary: How to build an autocompletion service with geographical context using solr

# Super flexible GeoAutoComplete with Solr #

In an inspiring article [Cominvent AS](http://www.cominvent.com/2012/01/25/super-flexible-autocomplete-with-solr/) presented us how to use [Solr](https://lucene.apache.org/solr/) power to implement autocomplete feature. We are going to present you how to add a geographical component to this suggestion.

1. Download and unpack Solr if you have not already [http://www.apache.org/dyn/closer.cgi/lucene/solr/](http://www.apache.org/dyn/closer.cgi/lucene/solr/)
2. Download and unpack [mappy-geoautocomplete.zip]({filename}/resources/mappy-autocomplete.zip)
3. Cd to the autocomplete folder, open README.TXT and follow the instructions. When done you will have Solr up and running with the example data indexed into the “acgeo” core.
4. When you browse to http://localhost:8000/ and start typing, you will see a map and countries and cities suggested

As ranking factor, we use a combination of the population of the countries and cities, the textual relevancy and, that is the main point of our article, the proximity to the center of the map we display.
As the use of population and text relevancy has been explained in [Cominvent As](http://www.cominvent.com/2012/01/25/super-flexible-autocomplete-with-solr/) article, let's focus on the geographical part of the score.
First we need to store the coordinates for each city and country. Thus we add longitude (lng) and latitude (lat) fields in our schema.xml

    :::xml
    <field name="lng" type="float" indexed="true" stored="true" omitNorms="true" required="true"/>
    <field name="lat" type="float" indexed="true" stored="true" omitNorms="true" required="true"/>

Then we need to modify solrconfig.xml

    :::xml
    <requestHandler class="solr.SearchHandler" name="acgeo" default="true" >
        <lst name="defaults">
            <str name="defType">edismax</str>
            <str name="rows">10</str>
            <str name="fl">*,score</str>
            <str name="qf">name^30 textng^50.0</str>
            <str name="pf">textnge^50.0</str>
            <str name="bf">product(log(sum(population,1)),100)^20</str>
            <!-- Define relative importance between types. May be overridden per request by e.g. &personboost=120 -->
            <str name="boost">product(product(map(query($type1query),0,0,1,$type1boost),map(query($type2query),0,0,1,$type2boost),map(query($type3query),0,0,1,$type3boost),map(query($type4query),0,0,1,$type4boost),$typeboost), geoboost($eps,$mu,$lat_min,$lng_min,$lat_max,$lng_max,lat,lng))</str>
            <double name="typeboost">1.0</double>

            <str name="type1query">type:"Countries"</str>
            <double name="type1boost">0.9</double>
            <str name="type2query">type:"Cities"</str>
            <double name="type2boost">0.5</double>
            <str name="type3query">type:"NA"</str>
            <double name="type3boost">0.0</double>
            <str name="type4query">type:"NA"</str>
            <double name="type4boost">0.0</double>

            <str name="lng_min">0</str>
            <str name="lat_min">0</str>
            <str name="lng_max">0</str>
            <str name="lat_max">0</str>
            <str name="eps">0.1</str>
            <str name="mu">1.0</str>

            <str name="debugQuery">false</str>
        </lst>
    </requestHandler>

Now that our Solr is prepared to manage request with coordinates, we obviously have to send it.

    :::js
    $.ajax({
          'url': 'http://localhost:8983/solr/acgeo/select?',
          'delay': 1,
          'dataType': "jsonp",
          'data': {
            'q': request.term,
            wt: "json",
            "json.wrf" : "callback",
            "rows": 5,
            'lat_min': myMap.getBounds().getSouth(),
            'lat_max': myMap.getBounds().getNorth(),
            'lng_min': myMap.getBounds().getWest(),
            'lng_max': myMap.getBounds().getEast()
          },
    ...)

Even if Solr [FunctionQuery](http://wiki.apache.org/solr/FunctionQuery) gives us a set of possibility, it may not fit our particular needs. In that case we can easily extend the list of available functions by writing our own in Java. Let's implement a `geoboost` function that is equal to `1` inside a given bounding box, and that is decreasing until `epsilon` outside the bounding box. The decreasing speed is configurable via parameter `mu` (A plot of this function is available [here]({filename}/images/geoboost.png))

    geoboost(epsilon, mu, lat_min, lng_min, lat_max, lng_max)

We have to write a parser (i.e. a class implementing [org.apache.solr.search.ValueSourceParser](http://wiki.apache.org/solr/SolrPlugins#ValueSourceParser) that reads the value from the left to the right)

    :::java
    public class GeoBoostValueParser extends ValueSourceParser {

        @Override
        public ValueSource parse(FunctionQParser fp) throws SyntaxError {
            float eps = fp.parseFloat();
            float mu = fp.parseFloat();
            float latmin = fp.parseFloat();
            float lngmin = fp.parseFloat();
            float latmax = fp.parseFloat();
            float lngmax = fp.parseFloat();
        	ValueSource lat = fp.parseValueSource();
        	ValueSource lng = fp.parseValueSource();
        	return new GeoBoostFunction(eps,mu,latmin,lngmin,latmax,lngmax,lat,lng);
        }
    }

And the class that does the real job, where the result is returned by `public FunctionValues getValues()`

    :::java
    public class GeoBoostFunction extends ValueSource {
      protected ValueSource lat, lng;
      protected float latmin, lngmin, latmax, lngmax;
      protected float eps, mu;

      public GeoBoostFunction(float eps, float mu, float latmin, float lngmin, float latmax, float lngmax, ValueSource lat, ValueSource lng) {
        ...
      }

      @Override
      public FunctionValues getValues(Map context, AtomicReaderContext readerContext) throws IOException {
            return new FloatDocValues(this) {
                @Override
                public float floatVal(int doc) {
                    return boost(doc, latvals, lngvals);
                }
                ...
            };
      }
      ...
    }//class GeoBoostFunction

Once the function and parser are written and compiled, we register the function in the sorlconfig.xml by adding the path to our *.jar and specifying our parser.

    :::xml
    <config>
        ...
        <lib path="lib/lbs-geoboost.jar" />
        <valueSourceParser name="geoboost" class="com.mappy.lbs.solr.search.function.GeoBoostValueParser" />
        ...
    </config>

Now we can run and test our configuration.

Using the default bounding box value (0,0,0,0) `http://127.0.0.1:8983/solr/acgeo/select?q=pa&wt=json&` leads to

    :::json
    {"responseHeader":
        {"status":0,"QTime":21},
        "response":
            {"numFound":97,
             "start":0,
             "docs":
                [{"name":"Pakistan"},
                 {"name":"São Paulo"},
                 {"name":"Paraguay"},
                 {"name":"Papua New Guinea"},
                 {"name":"Palestine"},
                 {"name":"Panama"},
                 {"name":"Paris"},
                 {"name":"Patna"},
                 {"name":"Palembang"},
                 {"name":"Padang"}
                ]
            }
    }


Using a bounding box around Paris `http://127.0.0.1:8983/solr/acgeo/select?q=pa&wt=json&lat_min=48&lat_max=48.5&lng_min=2&lng_max=2.5` leads to

    :::json
    {"responseHeader":
        {"status":0,"QTime":8},
         "response":
            {"numFound":97,
             "start":0,
             "docs":
                [{"name":"Paris"},
                 {"name":"Sant Andreu de Palomar"},
                 {"name":"Pakistan"},
                 {"name":"Palma"},
                 {"name":"São Paulo"},
                 {"name":"Paraguay"},
                 {"name":"Papua New Guinea"},
                 {"name":"Palestine"},
                 {"name":"Panama"},
                 {"name":"Patna"}
                 ]
            }
    }
