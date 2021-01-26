import sys
from redis import Redis
from rq import Queue



from tasks import slow_func


q = Queue(connection=Redis(host='redis'))

q.enqueue(slow_func, 5)

