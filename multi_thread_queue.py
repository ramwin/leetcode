import threading


class ByteQueue:
    """基于 bytearray 的单生产者单消费者字节队列
    
    - send: 缓冲区满时抛出 BufferError
    - read: 缓冲区空时返回 None
    - 使用 head 和 tail 位置关系判断空/满
    """
    
    def __init__(self, capacity: int = 1024):
        # 实际容量 +1，用于区分空和满（浪费一个位置）
        self._buffer = bytearray(capacity + 1)
        self._capacity = capacity
        self._head = 0   # 读取位置
        self._tail = 0   # 写入位置
        
        self._lock = threading.Lock()
    
    def send(self, byte: int):
        """发送一个字节 (0-255)，缓冲区满时抛出 BufferError"""
        if not isinstance(byte, int) or not (0 <= byte <= 255):
            raise ValueError("byte must be an integer between 0 and 255")
        
        with self._lock:
            next_tail = (self._tail + 1) % len(self._buffer)
            if next_tail == self._head:
                raise BufferError("buffer is full")
            
            self._buffer[self._tail] = byte
            self._tail = next_tail
    
    def read(self) -> int | None:
        """读取一个字节，缓冲区空时返回 None"""
        with self._lock:
            if self._head == self._tail:
                return None
            
            byte = self._buffer[self._head]
            self._head = (self._head + 1) % len(self._buffer)
            
            return byte
