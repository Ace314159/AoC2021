import operator

with open("inputs/16.txt") as f:
    packets_str = f.read().strip()
byte_len = len(packets_str) * 4
packets = f"{{0:0{byte_len}b}}".format(int(packets_str, 16))


def parse_packet(i):
    def get_str(i, str_len):
        end = i + str_len
        return packets[i:end], end

    def get_int(i, int_len):
        s, new_i = get_str(i, int_len)
        return int(s, 2), new_i

    ret_version, i = get_int(i, 3)
    ret_type_id, i = get_int(i, 3)
    if ret_type_id == 4:
        final_num = ""
        while True:
            num, i = get_str(i, 5)
            final_num += num[1:]
            if num[0] == "0":
                break
        ret = int(final_num, 2)
    else:
        length_type_id, i = get_int(i, 1)
        ret = []
        if length_type_id == 0:
            bit_length, i = get_int(i, 15)
            end = i + bit_length
            while i < end:
                version, type_id, sub_packet, i = parse_packet(i)
                ret.append((version, type_id, sub_packet))
        else:
            num_sub_packets, i = get_int(i, 11)
            for _ in range(num_sub_packets):
                version, type_id, sub_packet, i = parse_packet(i)
                ret.append((version, type_id, sub_packet))
    return ret_version, ret_type_id, ret, i


def part_one():
    def get_version_sum(packet):
        version, type_id, ret = packet
        if type(ret) == list:
            return version + sum(get_version_sum(sub_packet) for sub_packet in ret)
        return version

    version, type_id, ret, i = parse_packet(0)
    return get_version_sum((version, type_id, ret))


def part_two():
    def eval_packet(type_id, ret):
        ops = {
            0: (operator.add, 0),
            1: (operator.mul, 1),
            2: (min, float("inf")),
            3: (max, float("-inf")),
            5: operator.gt,
            6: operator.lt,
            7: operator.eq,
        }
        if type_id < 4:
            fn, init = ops[type_id]
            ans = init
            for version, type_id, sub_ret in ret:
                ans = fn(ans, eval_packet(type_id, sub_ret))
        elif type_id == 4:
            ans = ret
        else:
            fn = ops[type_id]
            (first_ver, first_type_id, first_ret), (second_ver, second_type_id, second_ret) = ret
            first_val = eval_packet(first_type_id, first_ret)
            second_val = eval_packet(second_type_id, second_ret)
            ans = int(fn(first_val, second_val))
        return ans

    version, type_id, ret, i = parse_packet(0)
    return eval_packet(type_id, ret)


print(part_one())
print(part_two())
