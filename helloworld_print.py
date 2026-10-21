import random
import sys
import time


def HelloWorld(_=None):
    """Blurts out random 1s and 0s for ~5 seconds."""
    duration = 5
    end_time = time.time() + duration

    try:
        while time.time() < end_time:
            line_len = random.randint(20, 80)
            print("".join(random.choice("01") for _ in range(line_len)), end="\r", flush=True)

        # leave it on a "final" corrupted frame
        print("")
    except KeyboardInterrupt:
        print("")


if __name__ == "__main__":
    arg = sys.argv[1] if len(sys.argv) > 1 else None
    HelloWorld(arg)
