# microcosm-metrics

Opinionated metrics configuration.

Designed primary to support [DataDog statsd](http://docs.datadoghq.com/guides/dogstatsd/), but some
effort has been made to support [vanilla statsd](https://github.com/etsy/statsd).


## Usage

 1. Configure a metrics client:

        # either use vanilla statsd
        graph.use("statsd")

        # or use the datadog implementation
        graph.use("datadog_statsd")

 2. In either case, use the resulting `graph.metrics` client:

        metrics.increment("foo")


## Decorators

The two most common metrics usages are supported via decorator interfaces.

To time function calls, use:

    @graph.metrics_timing("my_func")
    def my_func():
        pass

To count function outcomes, use:

    @graph.metrics_counting("my_func")
    def my_func():
        pass

For counting, the default behavior is to count function *calls*. To count different outcomes,
use a custom `Classifier`:

    class TruthyClassifier(Classifier):

        def label_result(self, result):
            return "truthy" if bool(result) else "falsey"

        def label_error(self, error):
            return None

Then pass the classifier class to the counting decorator:

    @graph.metrics_counting("my_func", classifier=TruthyClassifier)
    def my_func():
        pass


## StatsD Testing

First, run the `statsd`. For example, using Docker:

    docker run -d --name graphite \
        -p 80:80 -p 2003-2004:2003-2004 -p 2023-2024:2023-2024 -p 8125:8125/udp -p 8126:8126 \
        hopsoft/graphite-statsd

Then, use the included CLIT to validate connectivity:

    publish-metric --statsd statsd --host $(docker-machine ip default)

The resulting metric should appear in the `graphite` dashboard.


## DataDog Testing

First, run the `DataDog Agent` (requires an `API_KEY`). For example, using Docker:

    docker run -d --name datadog-agent -p 8125:8125/udp -e API_KEY=${API_KEY} datadog/docker-dd-agent:latest

Then, use the included CLI to validate connectivity:

    publish-metric --statsd datadog --host $(docker-machine ip default)

The resulting metric should appear in `DataDog` "Metric Summary" right away.
