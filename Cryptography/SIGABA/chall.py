# SIGABA Cipher Challenge
# 
# Background: The SIGABA (also known as ECM Mark II or CSP-889/2900) was one
# of the most secure cipher machines of World War II, used by the United States.
# Unlike the German Enigma, SIGABA was never broken during wartime operations.

from secret import FLAG

class SigabaSimulator:
    def __init__(self, rotor_settings, control_settings, index_settings):
        self.cipher_rotors = rotor_settings
        self.control_rotors = control_settings
        self.index_rotors = index_settings
        # You dont need these (these are correct exept the last one)
        self.cipher_positions = [0, 0, 0, 0, 0]
        self.control_positions = [0, 0, 0, 0, 0]
        self.index_positions = [1, 2, 3, 4, 5]
        # or this
        self.step_pattern = [] 
        
    def set_positions(self, cipher_pos, control_pos, index_pos):
        self.cipher_positions = cipher_pos
        self.control_positions = control_pos
        self.index_positions = index_pos
    
    def step_rotors(self):
        active_rotors = self._get_active_rotors()
        
        for i in range(5):
            if i in active_rotors:
                self.cipher_positions[i] = (self.cipher_positions[i] + self.step_pattern[i]) % 26
        
        self.control_positions[0] = (self.control_positions[0] + 1) % 26
        if self.control_positions[0] == 0:
            self.control_positions[1] = (self.control_positions[1] + 1) % 26
            if self.control_positions[1] == 0:
                self.control_positions[2] = (self.control_positions[2] + 1) % 26
    
    def _get_active_rotors(self):
        control_outputs = []
        
        for i in range(5):
            pos = self.control_positions[i]
            output = (self.control_rotors[i][(i + pos) % 26] - pos) % 26
            control_outputs.append(output)
        
        index_inputs = [x % 10 for x in control_outputs]
        active_rotors = []
        
        for input_val in index_inputs:
            if input_val < 5:
                for i in range(5):
                    pos = self.index_positions[i]
                    output = (self.index_rotors[i][(input_val + pos) % 26] - pos) % 26
                    if output < 5:
                        active_rotors.append(output)
        
        return list(set(active_rotors))
    
    def encrypt_char(self, char):
        if not char.isalpha():
            return char
            
        char_num = ord(char.upper()) - ord('A')
        
        self.step_rotors()
        
        for i in range(5):
            pos = self.cipher_positions[i]
            char_num = (self.cipher_rotors[i][(char_num + pos) % 26] - pos) % 26
        
        return chr(char_num + ord('A'))
    
    def encrypt(self, message):
        return ''.join(self.encrypt_char(c) for c in message)

cipher_rotors = [
    [24, 17, 20, 7, 16, 18, 11, 3, 15, 23, 13, 6, 9, 2, 1, 22, 0, 14, 19, 10, 25, 5, 8, 21, 12, 4],
    [16, 5, 1, 7, 24, 15, 3, 20, 13, 18, 10, 2, 25, 14, 19, 9, 21, 4, 0, 17, 8, 23, 11, 22, 12, 6],
    [11, 4, 21, 10, 23, 19, 17, 8, 25, 14, 15, 1, 5, 2, 9, 20, 0, 13, 24, 22, 7, 12, 6, 18, 16, 3],
    [9, 5, 8, 25, 21, 20, 1, 15, 13, 17, 6, 10, 11, 24, 23, 16, 4, 22, 14, 0, 19, 3, 2, 12, 7, 18],
    [8, 13, 14, 0, 21, 17, 5, 10, 2, 19, 24, 15, 16, 18, 11, 3, 4, 25, 12, 23, 6, 7, 9, 20, 22, 1]
]

control_rotors = [
    [3, 20, 10, 17, 24, 8, 13, 6, 9, 11, 5, 16, 7, 22, 23, 15, 2, 25, 21, 1, 14, 4, 19, 12, 0, 18],
    [19, 21, 25, 3, 23, 16, 9, 13, 17, 8, 22, 4, 0, 5, 11, 14, 20, 10, 15, 2, 1, 24, 6, 12, 7, 18],
    [24, 17, 0, 3, 25, 5, 9, 14, 6, 13, 2, 1, 19, 10, 22, 18, 12, 20, 11, 4, 21, 16, 8, 7, 23, 15],
    [5, 17, 16, 13, 21, 3, 6, 19, 25, 23, 0, 14, 9, 8, 20, 11, 1, 18, 24, 10, 15, 4, 2, 22, 7, 12],
    [12, 24, 21, 13, 17, 22, 7, 16, 23, 9, 18, 25, 0, 5, 1, 3, 8, 2, 20, 19, 14, 11, 10, 4, 15, 6]
]

index_rotors = [
    [7, 12, 19, 1, 23, 16, 5, 2, 9, 0, 11, 17, 24, 20, 14, 13, 6, 21, 10, 15, 3, 25, 8, 18, 4, 22],
    [13, 25, 9, 7, 6, 17, 2, 23, 12, 24, 18, 22, 1, 14, 20, 5, 0, 8, 21, 11, 15, 4, 10, 16, 19, 3],
    [22, 18, 16, 1, 13, 24, 9, 6, 25, 19, 2, 14, 7, 0, 11, 23, 21, 17, 3, 26, 5, 12, 8, 15, 4, 10],
    [20, 11, 5, 25, 14, 9, 22, 15, 8, 3, 13, 24, 0, 17, 7, 21, 16, 10, 2, 19, 6, 1, 4, 23, 18, 12],
    [16, 5, 11, 22, 8, 0, 25, 20, 17, 13, 3, 2, 23, 14, 9, 6, 19, 12, 24, 18, 7, 1, 10, 21, 4, 15]
]
# And of course you will not need these to :)
cipher_pos = []    
control_pos = []    
index_pos = []    

sigaba = SigabaSimulator(cipher_rotors, control_rotors, index_rotors)
sigaba.set_positions(cipher_pos, control_pos, index_pos)

flag = FLAG

encrypted_flag = sigaba.encrypt(flag)
print("Encrypted flag:", encrypted_flag)