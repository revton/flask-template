import multiprocessing

workers = multiprocessing.cpu_count() * 2 + 1
threads = multiprocessing.cpu_count() * 2 + 1
timeout = 300
worker_class = "gevent"
