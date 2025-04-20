import os


class VideoStream:
    def get_frame_lengths(self, filename):
        with open(filename, 'rb') as f:
            data = f.read()

        frame_lengths = []
        # 特化給movie 他的編碼會帶前綴 必須計算前綴長度是多少 其他一般的mjpeg不會有前綴(0)
        start = 0
        first = False
        diff = 0
        # 到這裡
        while True:
            # 尋找下一幀的開始（0xFF 0xD8）
            start = data.find(b'\xFF\xD8', start)
            if first == False:
                first = True
                diff = start
            if start == -1:
                break

            # 尋找這一幀的結束（0xFF 0xD9）
            end = data.find(b'\xFF\xD9', start)
            if end == -1:
                break

            # 計算這一幀的長度
            frame_length = end - start + 2
            frame_lengths.append(frame_length)

            # 移動到下一幀
            start = end + 2

        return frame_lengths, diff

    def __init__(self, filename):
        self.cnt = 0
        self.filename = filename
        self.frame_lengths, self.diff = self.get_frame_lengths(self.filename)
      #  for i, length in enumerate(self.frame_lengths):
        #  print(f'Frame {i+1}: {length} bytes')
        try:
            self.file = open(filename, 'rb')

           # data = self.file.read()
           # new_data = b'\x30\x36\x30\x31\x34'
           # with open(filename, 'wb') as f:
           #     f.write(new_data + data)
           # hex_data = self.file.read(100)
           # print(' '.join(hex_data))
        except:
            raise IOError
        self.frameNum = 0

# 將字節轉換為十六進位並打印

    def nextFrame(self):
        """Get next frame."""
       # data = []
        if self.diff != 0:
            data = self.file.read(
                self.diff)  # Get the framelength from the first 5 bits
       # if data:
        framelength = self.frame_lengths[self.cnt]
        self.cnt = self.cnt+1
        data = self.file.read(framelength)
        self.frameNum += 1
        return data

    def frameNbr(self):
        """Get frame number."""
        return self.frameNum
