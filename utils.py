class utils:
    def reversed(num: int) -> int:
        num_str = str(num)
        size = len(num_str)
        ret = num_str[size::-1]
        return ret
    def formatter(num: int):
        binary = bin(num)
        octal = oct(num)
        return (binary, octal)