# Create your tasks here

from celery import shared_task
import time, math
def heavy_computation():
    # Make this take longer by running until a minimum duration
    min_seconds = 20  # adjust as needed
    total_start = time.time()
    iterations = 0
    primes_found = 0
    n = 5_000_000  # heavier per-iteration load
    while True:
        start_ts = time.time()
        sieve = bytearray(b'\x01') * (n + 1)
        sieve[0:2] = b'\x00\x00'
        limit = int(math.isqrt(n))
        for p in range(2, limit + 1):
            if sieve[p]:
                start = p * p
                step = p
                sieve[start:n + 1:step] = b'\x00' * (((n - start) // step) + 1)
        primes_found = int(sum(sieve))
        iterations += 1
        iter_time = time.time() - start_ts
        elapsed = time.time() - total_start
        print(f'Iteration {iterations}: computed {primes_found} primes up to {n} in {iter_time:.2f}s (total {elapsed:.2f}s)')
        if elapsed >= min_seconds:
            break
    print(f'Computed {primes_found} primes up to {n} in {time.time() - total_start:.2f}s after {iterations} iterations')

@shared_task
def notify_sending(x, y):
    heavy_computation()
    print('celery task notify_sending called with', x, y)
    return x + y

# celery -A project worker -l info 