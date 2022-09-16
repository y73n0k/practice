from Crypto.Util.Padding import pad
from Crypto.Util.number import getPrime, isPrime
from Crypto.Cipher import AES
from secrets import randbelow
from hashlib import sha256

FLAGS = [
    'jctf{red_flags_and_fake_flags_form_an_equivalence_class}',
    'jctf{clicking_cant_help_you_now}',
    'jctf{just_cat_the_fish}',
    'jctf{making_fake_flags_is_more_fun_than_making_real_flags}',
    'jctf{powered_by_Flask_tm}',
    'jctf{sourcelesswebaphobia}',
    'jctf{cats_love_fish_fake_flags_and_hash_browns}',
    'jctf{always_eat_potatoes_for_breakfast}',
    'jctf{%s}',
    'jctf{en_passant_is_forced}',
    'jctf{the_fitness_gram_pacer_test_is_too_long_for_a_flag_\x07}',
    'jctf{never_gonna_give_you_up}',
    'jctf{never_gonna_let_you_down}',
    'jctf{you_know_the_rules_and_so_do_I}',
    'jctf{https://www.youtube.com/watch?v=dQw4w9WgXcQ}',
    'jctf{i_never_use_salt_on_my_potatoes}',
    'jctf{the_equivalence_class_of_fake_flags_and_red_flags_of_course_forms_a_partition_too}',
    'jctf{fake_flags_are_fun}',
    'jctf{you\'ve_heard_of_zyphen_chamber_but_have_you_heard_of_siphon_chamber?_coming_soon_(tm)_to_a_daily_challenge_near_you_soon}',
    'jctf{what_even_is_an_equivalence_class}',
    'jctf{?????????????????you_can\'t_stop_me?????????????????}',
    'jctf{watch_me_put_an_emote_in_a_flag_to_screw_nitro_users_:rooPuzzlerDevil:}',
    'jctf{⚑}',
    'jctf{dont_dos_my_server_please_ill_be_sad}',
    'jctf{Also_play_terraria!}',
    'jctf{Also_play_outer_wilds!}',
    'jctf{Also_play_minecraft!}',
    'jctf{one_flag_to_rule_them_all_one_flag_to_find_them}',
    'jctf{one_flag_to_bring_them_all_and_in_the_darkness_bind_them}',
    'jctf{a_hacker_is_just_someone_that_wears_a_hoodie_on_the_internet}',
    'jctf{powered_by_python}',
    'jctf{powered_by_caffeine}',
    'jctf{im_scared_of_phobias}',
    'jctf{0._the_programmer_started_to_cuss}',
    'jctf{1._for_falling_asleep_was_a_fuss}',
    'jctf{2._as_he_lay_there_in_bed}',
    'jctf{3._whirling_round_in_his_head}',
    'jctf{4._was_while(!asleep)sheep++;}',
    'jctf{Also_play_elden_ring!}',
]

class LFSR:
    def __init__(self) -> None:
        # This is 128 times more random than urandom!
        self.state = [randbelow(q) for _ in range(128)]
        self.taps = [0, 7, 36, 57, 95, 104, 127]
    
    def __next__(self):
        s = self.state[0]
        self.state = self.state[1:] + [sum(self.state[t] for t in self.taps) % q]
        return s


def H(m):
    return int.from_bytes(sha256(m).digest(), 'big')

def sign(m):
    k = next(nonces)
    r = pow(g, k, p) % q
    s = (H(m) + r*x) * pow(k, -1, q) % q
    return r, s

def verify(m, r, s):
    u = pow(s, -1, q)
    return pow(g, u * H(m), p) * pow(y, u * r, p) % p % q == r


if __name__ == '__main__':
    q, g = 0, 2
    while not isPrime(p := 2*q + 1) or pow(g, q, p) != 1:
        q = getPrime(256)

    x = randbelow(q)
    y = pow(g, x, p)
    nonces = LFSR()

    flag = b'ictf{REDACTED}'
    key = next(nonces).to_bytes(32, 'big')
    aes = AES.new(key[:16], AES.MODE_CBC, key[16:])
    enc = aes.encrypt(pad(flag, 16))

    sigs = [sign(FLAGS[i % len(FLAGS)].encode()) for i in range(256)]
    with open('out.txt', 'w') as file:
        file.writelines([
            f"sigs = {str(sigs).replace(' ', '')}\n",
            f"enc = bytes.fromhex('{enc.hex()}')\n",
            f"p = {p}\n",
            f"y = {y}"
        ])
