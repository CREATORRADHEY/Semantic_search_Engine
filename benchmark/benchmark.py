from benchmark.timer import Timer


class Benchmark:

    @staticmethod
    def run(name: str, function, *args, **kwargs):

        timer = Timer()

        timer.start()

        result = function(
            *args,
            **kwargs
        )

        timer.stop()

        print("=" * 60)

        print(name)

        print(f"Elapsed : {timer.elapsed:.6f} seconds")

        print("=" * 60)

        return result