# Create your tasks here

from celery import shared_task
import time, math

def heavy_computation():
    start_ts = time.time()
    n = 500_000  # increase for more load
    sieve = bytearray(b'\x01') * (n + 1)
    sieve[0:2] = b'\x00\x00'
    limit = int(math.isqrt(n))
    for p in range(2, limit + 1):
        if sieve[p]:
            start = p * p
            step = p
            sieve[start:n + 1:step] = b'\x00' * (((n - start) // step) + 1)
    primes_found = int(sum(sieve))
    print(f'Computed {primes_found} primes up to {n} in {time.time() - start_ts:.2f}s')


@shared_task
def notify_sending(x, y):
    heavy_computation()
    print('celery task notify_sending called with', x, y)
    return x + y

# celery -A project worker -l info 