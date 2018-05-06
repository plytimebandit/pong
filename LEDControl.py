import spi


class LEDControl:

    SWITCH_ON = True
    SWITCH_OFF = False
    FIELD_SIZE = 8        # 8x8 pixels
    TOTAL_MATRICES = 4    # number of daisy chained matrices

    def __init__(self):
        self.max7219 = spi.SPI(clk=11, cs=8, mosi=10, miso=None)

        self.buffer = []
        for m in range(self.TOTAL_MATRICES):
            one_matrix_buffer = []
            for c in range(self.FIELD_SIZE):
                one_matrix_buffer.append([False] * self.FIELD_SIZE)
            self.buffer.append(one_matrix_buffer)

        self.reset()
        self.init()

    def __del__(self):
        self.reset()

    def init(self):
        """ Set the scan limit register and disable shutdown mode"""
        self.write(int("1011", 2), ["00000111"] * self.TOTAL_MATRICES)
        self.write(int("1100", 2), ["00000001"] * self.TOTAL_MATRICES)

    def reset(self):
        """ Zero out all registers """
        for register in range(16):
            packet = register
            self.write(packet, ["0"*8] * self.TOTAL_MATRICES)

    def write(self, register, values):
        register_binary16 = "{:0>8}".format("{:b}".format(register))
        packet = ""
        for v in values:
            packet += register_binary16 + v

        self.max7219.put(int(packet, 2), 16 * self.TOTAL_MATRICES)

    def clear(self):
        for register in range(8):
            packet = register
            self.write(packet, ["0"*8] * self.TOTAL_MATRICES)

        for matrix in self.buffer:
            for col in matrix:
                for row in col:
                    col[row] = self.SWITCH_OFF

    def set_led(self, col, row, switch):
        """ col=1, row=1 is the first LED of the matrix """
        idx = self.matrix_index(col, row)
        self.buffer[idx][(col-1) % self.FIELD_SIZE][(row-1) % self.FIELD_SIZE] = switch

    @staticmethod
    def matrix_index(col, row):
        """ col=1, row=1 is the first LED of the matrix """
        """ Handles only 16x16 matrices """
        idx = 1 if col > 8 else 0
        idx += 2 if row > 8 else 0
        return idx

    def repaint(self):
        for col in range(self.FIELD_SIZE):
            register = col + 1

            row_values = []
            for matrixIndex in range(self.TOTAL_MATRICES-1, -1, -1):
                row_val = "".join(map(lambda r: "1" if r else "0", self.buffer[matrixIndex][col]))
                row_values.append(row_val)

            self.write(register, row_values)
