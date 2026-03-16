"""多生产者多消费者字节队列 - 单锁实现

这是 Python 中最简单且正确的方案。
如需高性能无锁队列，请使用 C/C++ 扩展（如 `libringbuf`、`boost::lockfree::spsc_queue` 等）。
"""
import threading


class ByteQueue:
    def __init__(self, capacity: int = 1024):
        self._buffer = bytearray(capacity + 1)  # +1 区分空/满
        self._capacity = capacity
        self._head = 0
        self._tail = 0
        self._lock = threading.Lock()
    
    def send(self, byte: int):
        """发送一个字节，满时抛 BufferError"""
        if not isinstance(byte, int) or not (0 <= byte <= 255):
            raise ValueError("byte must be 0-255")
        
        with self._lock:
            next_tail = (self._tail + 1) % len(self._buffer)
            if next_tail == self._head:
                raise BufferError("buffer is full")
            
            self._buffer[self._tail] = byte
            self._tail = next_tail
    
    def read(self) -> int | None:
        """读取一个字节，空时返回 None"""
        with self._lock:
            if self._head == self._tail:
                return None
            
            byte = self._buffer[self._head]
            self._head = (self._head + 1) % len(self._buffer)
            return byte
