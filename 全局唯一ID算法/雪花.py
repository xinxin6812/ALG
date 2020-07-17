import time

# 注 机器ID占位5 这也就意味者十进制下编号不能超过31  将机器ID与机房ID合并，最大三个机房即00 10 20 每个机房的数值 + 1 即是机器ID  备用 30 31
WORKER_ID_BITS = 5
SEQUENCE_BITS = 12

# 最大取值计算
MAX_WORKER_ID = -1 ^ (-1 << WORKER_ID_BITS)

# 移位偏移计算
WORKER_ID_SHIFT = SEQUENCE_BITS
TIMESTAMP_LEFT_SHIFT = SEQUENCE_BITS + WORKER_ID_BITS
# print(WORKER_ID_SHIFT, TIMESTAMP_LEFT_SHIFT)

# 序号循环掩码
SEQUENCE_MASK = -1 ^ (-1 << SEQUENCE_BITS)
# print(SEQUENCE_MASK)

# 起始时间
TWEPOCH = 1594977661913


class IdWorker(object):

    def __init__(self, worker_id, sequence=0):
        """

        :param worker_id: 机房和机器的ID 最大编号可为00 - 31  实际使用范围 00 - 29  备用 30 31
        :param sequence: 初始码
        """
        if worker_id > MAX_WORKER_ID or worker_id < 0:
            raise ValueError('worker_id值越界')

        self.worker_id = worker_id
        self.sequence = sequence
        self.last_timestamp = -1  # 上次计算的时间戳

    def get_timestamp(self):
        """
        生成毫秒级时间戳
        :return: 毫秒级时间戳
        """
        return int(time.time() * 1000)

    def wait_next_millis(self, last_timestamp):
        """
        等到下一毫秒
        """
        timestamp = self.get_timestamp()
        while timestamp <= last_timestamp:
            timestamp = self.get_timestamp()
        return timestamp

    def get_id(self):
        """"""
        timestamp = self.get_timestamp()
        # 判断服务器的时间是否发生了错乱或者回拨
        if timestamp < self.last_timestamp:
            # 如果服务器发生错乱 应该抛出异常
            # 此处待完善
            pass

        if timestamp == self.last_timestamp:
            self.sequence = (self.sequence + 1) & SEQUENCE_MASK
            if self.sequence == 0:
                timestamp = self.wait_next_millis(self.last_timestamp)
        else:
            self.sequence = 0
        self.last_timestamp = timestamp
        new_id = ((timestamp - TWEPOCH) << TIMESTAMP_LEFT_SHIFT) | (self.worker_id << WORKER_ID_SHIFT) | self.sequence
        return new_id


if __name__ == '__main__':
    # 测试效率
    import datetime
    worker = IdWorker(worker_id=1, sequence=0)
    ids = []
    start = datetime.datetime.now()
    for i in range(1000000):
        new_id = worker.get_id()
        ids.append(new_id)
    end = datetime.datetime.now()
    spend_time = end - start
    print(spend_time, len(ids), len(set(ids)))


