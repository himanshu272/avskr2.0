# Stubs for redis.client (Python 2)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

SYM_EMPTY = ... # type: Any

def list_or_args(keys, args): ...
def timestamp_to_datetime(response): ...
def string_keys_to_dict(key_string, callback): ...
def dict_merge(*dicts): ...
def parse_debug_object(response): ...
def parse_object(response, infotype): ...
def parse_info(response): ...

SENTINEL_STATE_TYPES = ... # type: Any

def parse_sentinel_state(item): ...
def parse_sentinel_master(response): ...
def parse_sentinel_masters(response): ...
def parse_sentinel_slaves_and_sentinels(response): ...
def parse_sentinel_get_master(response): ...
def pairs_to_dict(response): ...
def pairs_to_dict_typed(response, type_info): ...
def zset_score_pairs(response, **options): ...
def sort_return_tuples(response, **options): ...
def int_or_none(response): ...
def float_or_none(response): ...
def bool_ok(response): ...
def parse_client_list(response, **options): ...
def parse_config_get(response, **options): ...
def parse_scan(response, **options): ...
def parse_hscan(response, **options): ...
def parse_zscan(response, **options): ...
def parse_slowlog_get(response, **options): ...

class StrictRedis:
    RESPONSE_CALLBACKS = ... # type: Any
    @classmethod
    def from_url(cls, url, db=..., **kwargs): ...
    connection_pool = ... # type: Any
    response_callbacks = ... # type: Any
    def __init__(self, host=..., port=..., db=..., password=..., socket_timeout=..., socket_connect_timeout=..., socket_keepalive=..., socket_keepalive_options=..., connection_pool=..., unix_socket_path=..., encoding=..., encoding_errors=..., charset=..., errors=..., decode_responses=..., retry_on_timeout=..., ssl=..., ssl_keyfile=..., ssl_certfile=..., ssl_cert_reqs=..., ssl_ca_certs=...) -> None: ...
    def set_response_callback(self, command, callback): ...
    def pipeline(self, transaction=..., shard_hint=...): ...
    def transaction(self, func, *watches, **kwargs): ...
    def lock(self, name, timeout=..., sleep=..., blocking_timeout=..., lock_class=..., thread_local=...): ...
    def pubsub(self, **kwargs): ...
    def execute_command(self, *args, **options): ...
    def parse_response(self, connection, command_name, **options): ...
    def bgrewriteaof(self): ...
    def bgsave(self): ...
    def client_kill(self, address): ...
    def client_list(self): ...
    def client_getname(self): ...
    def client_setname(self, name): ...
    def config_get(self, pattern=...): ...
    def config_set(self, name, value): ...
    def config_resetstat(self): ...
    def config_rewrite(self): ...
    def dbsize(self): ...
    def debug_object(self, key): ...
    def echo(self, value): ...
    def flushall(self): ...
    def flushdb(self): ...
    def info(self, section=...): ...
    def lastsave(self): ...
    def object(self, infotype, key): ...
    def ping(self): ...
    def save(self): ...
    def sentinel(self, *args): ...
    def sentinel_get_master_addr_by_name(self, service_name): ...
    def sentinel_master(self, service_name): ...
    def sentinel_masters(self): ...
    def sentinel_monitor(self, name, ip, port, quorum): ...
    def sentinel_remove(self, name): ...
    def sentinel_sentinels(self, service_name): ...
    def sentinel_set(self, name, option, value): ...
    def sentinel_slaves(self, service_name): ...
    def shutdown(self): ...
    def slaveof(self, host=..., port=...): ...
    def slowlog_get(self, num=...): ...
    def slowlog_len(self): ...
    def slowlog_reset(self): ...
    def time(self): ...
    def append(self, key, value): ...
    def bitcount(self, key, start=..., end=...): ...
    def bitop(self, operation, dest, *keys): ...
    def bitpos(self, key, bit, start=..., end=...): ...
    def decr(self, name, amount=...): ...
    def delete(self, *names): ...
    def __delitem__(self, name): ...
    def dump(self, name): ...
    def exists(self, name): ...
    __contains__ = ... # type: Any
    def expire(self, name, time): ...
    def expireat(self, name, when): ...
    def get(self, name): ...
    def __getitem__(self, name): ...
    def getbit(self, name, offset): ...
    def getrange(self, key, start, end): ...
    def getset(self, name, value): ...
    def incr(self, name, amount=...): ...
    def incrby(self, name, amount=...): ...
    def incrbyfloat(self, name, amount=...): ...
    def keys(self, pattern=...): ...
    def mget(self, keys, *args): ...
    def mset(self, *args, **kwargs): ...
    def msetnx(self, *args, **kwargs): ...
    def move(self, name, db): ...
    def persist(self, name): ...
    def pexpire(self, name, time): ...
    def pexpireat(self, name, when): ...
    def psetex(self, name, time_ms, value): ...
    def pttl(self, name): ...
    def randomkey(self): ...
    def rename(self, src, dst): ...
    def renamenx(self, src, dst): ...
    def restore(self, name, ttl, value): ...
    def set(self, name, value, ex=..., px=..., nx=..., xx=...): ...
    def __setitem__(self, name, value): ...
    def setbit(self, name, offset, value): ...
    def setex(self, name, time, value): ...
    def setnx(self, name, value): ...
    def setrange(self, name, offset, value): ...
    def strlen(self, name): ...
    def substr(self, name, start, end=...): ...
    def ttl(self, name): ...
    def type(self, name): ...
    def watch(self, *names): ...
    def unwatch(self): ...
    def blpop(self, keys, timeout=...): ...
    def brpop(self, keys, timeout=...): ...
    def brpoplpush(self, src, dst, timeout=...): ...
    def lindex(self, name, index): ...
    def linsert(self, name, where, refvalue, value): ...
    def llen(self, name): ...
    def lpop(self, name): ...
    def lpush(self, name, *values): ...
    def lpushx(self, name, value): ...
    def lrange(self, name, start, end): ...
    def lrem(self, name, count, value): ...
    def lset(self, name, index, value): ...
    def ltrim(self, name, start, end): ...
    def rpop(self, name): ...
    def rpoplpush(self, src, dst): ...
    def rpush(self, name, *values): ...
    def rpushx(self, name, value): ...
    def sort(self, name, start=..., num=..., by=..., get=..., desc=..., alpha=..., store=..., groups=...): ...
    def scan(self, cursor=..., match=..., count=...): ...
    def scan_iter(self, match=..., count=...): ...
    def sscan(self, name, cursor=..., match=..., count=...): ...
    def sscan_iter(self, name, match=..., count=...): ...
    def hscan(self, name, cursor=..., match=..., count=...): ...
    def hscan_iter(self, name, match=..., count=...): ...
    def zscan(self, name, cursor=..., match=..., count=..., score_cast_func=...): ...
    def zscan_iter(self, name, match=..., count=..., score_cast_func=...): ...
    def sadd(self, name, *values): ...
    def scard(self, name): ...
    def sdiff(self, keys, *args): ...
    def sdiffstore(self, dest, keys, *args): ...
    def sinter(self, keys, *args): ...
    def sinterstore(self, dest, keys, *args): ...
    def sismember(self, name, value): ...
    def smembers(self, name): ...
    def smove(self, src, dst, value): ...
    def spop(self, name): ...
    def srandmember(self, name, number=...): ...
    def srem(self, name, *values): ...
    def sunion(self, keys, *args): ...
    def sunionstore(self, dest, keys, *args): ...
    def zadd(self, name, *args, **kwargs): ...
    def zcard(self, name): ...
    def zcount(self, name, min, max): ...
    def zincrby(self, name, value, amount=...): ...
    def zinterstore(self, dest, keys, aggregate=...): ...
    def zlexcount(self, name, min, max): ...
    def zrange(self, name, start, end, desc=..., withscores=..., score_cast_func=...): ...
    def zrangebylex(self, name, min, max, start=..., num=...): ...
    def zrangebyscore(self, name, min, max, start=..., num=..., withscores=..., score_cast_func=...): ...
    def zrank(self, name, value): ...
    def zrem(self, name, *values): ...
    def zremrangebylex(self, name, min, max): ...
    def zremrangebyrank(self, name, min, max): ...
    def zremrangebyscore(self, name, min, max): ...
    def zrevrange(self, name, start, end, withscores=..., score_cast_func=...): ...
    def zrevrangebyscore(self, name, max, min, start=..., num=..., withscores=..., score_cast_func=...): ...
    def zrevrank(self, name, value): ...
    def zscore(self, name, value): ...
    def zunionstore(self, dest, keys, aggregate=...): ...
    def pfadd(self, name, *values): ...
    def pfcount(self, name): ...
    def pfmerge(self, dest, *sources): ...
    def hdel(self, name, *keys): ...
    def hexists(self, name, key): ...
    def hget(self, name, key): ...
    def hgetall(self, name): ...
    def hincrby(self, name, key, amount=...): ...
    def hincrbyfloat(self, name, key, amount=...): ...
    def hkeys(self, name): ...
    def hlen(self, name): ...
    def hset(self, name, key, value): ...
    def hsetnx(self, name, key, value): ...
    def hmset(self, name, mapping): ...
    def hmget(self, name, keys, *args): ...
    def hvals(self, name): ...
    def publish(self, channel, message): ...
    def eval(self, script, numkeys, *keys_and_args): ...
    def evalsha(self, sha, numkeys, *keys_and_args): ...
    def script_exists(self, *args): ...
    def script_flush(self): ...
    def script_kill(self): ...
    def script_load(self, script): ...
    def register_script(self, script): ...

class Redis(StrictRedis):
    RESPONSE_CALLBACKS = ... # type: Any
    def pipeline(self, transaction=..., shard_hint=...): ...
    def setex(self, name, value, time): ...
    def lrem(self, name, value, num=...): ...
    def zadd(self, name, *args, **kwargs): ...

class PubSub:
    PUBLISH_MESSAGE_TYPES = ... # type: Any
    UNSUBSCRIBE_MESSAGE_TYPES = ... # type: Any
    connection_pool = ... # type: Any
    shard_hint = ... # type: Any
    ignore_subscribe_messages = ... # type: Any
    connection = ... # type: Any
    encoding = ... # type: Any
    encoding_errors = ... # type: Any
    decode_responses = ... # type: Any
    def __init__(self, connection_pool, shard_hint=..., ignore_subscribe_messages=...) -> None: ...
    def __del__(self): ...
    channels = ... # type: Any
    patterns = ... # type: Any
    def reset(self): ...
    def close(self): ...
    def on_connect(self, connection): ...
    def encode(self, value): ...
    @property
    def subscribed(self): ...
    def execute_command(self, *args, **kwargs): ...
    def parse_response(self, block=...): ...
    def psubscribe(self, *args, **kwargs): ...
    def punsubscribe(self, *args): ...
    def subscribe(self, *args, **kwargs): ...
    def unsubscribe(self, *args): ...
    def listen(self): ...
    def get_message(self, ignore_subscribe_messages=...): ...
    def handle_message(self, response, ignore_subscribe_messages=...): ...
    def run_in_thread(self, sleep_time=...): ...

class BasePipeline:
    UNWATCH_COMMANDS = ... # type: Any
    connection_pool = ... # type: Any
    connection = ... # type: Any
    response_callbacks = ... # type: Any
    transaction = ... # type: Any
    shard_hint = ... # type: Any
    watching = ... # type: Any
    def __init__(self, connection_pool, response_callbacks, transaction, shard_hint) -> None: ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, traceback): ...
    def __del__(self): ...
    def __len__(self): ...
    command_stack = ... # type: Any
    scripts = ... # type: Any
    explicit_transaction = ... # type: Any
    def reset(self): ...
    def multi(self): ...
    def execute_command(self, *args, **kwargs): ...
    def immediate_execute_command(self, *args, **options): ...
    def pipeline_execute_command(self, *args, **options): ...
    def raise_first_error(self, commands, response): ...
    def annotate_exception(self, exception, number, command): ...
    def parse_response(self, connection, command_name, **options): ...
    def load_scripts(self): ...
    def execute(self, raise_on_error=...): ...
    def watch(self, *names): ...
    def unwatch(self): ...
    def script_load_for_pipeline(self, script): ...

class StrictPipeline(BasePipeline, StrictRedis): ...
class Pipeline(BasePipeline, Redis): ...

class Script:
    registered_client = ... # type: Any
    script = ... # type: Any
    sha = ... # type: Any
    def __init__(self, registered_client, script) -> None: ...
    def __call__(self, keys=..., args=..., client=...): ...
