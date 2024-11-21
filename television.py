from tokenize import String


class Television:
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3
    def __init__(self):
        """Initialize the Television class"""
        self.status = False
        self.muted = False
        self.volume = self.MIN_VOLUME
        self.channel = self.MIN_CHANNEL
       # self.temp_volume= self.volume
    def power(self):
        """Change the power status of the TV"""
        self.status = not self.status

    def mute(self):
        """Change the mute status of the TV when TV is ON"""
        if self.status:
            self.muted = not self.muted

    def channel_up(self):
        """Increase the channel of the TV when TV is ON or decrease to MIN value when exceeding MAX value"""
        if self.status:
            if self.channel >= self.MAX_CHANNEL:
                self.channel = self.MIN_CHANNEL
            else:
                self.channel += 1

    def channel_down(self):
        """Decrease the channel of the TV when TV is ON or increase to Max value when exceeding MIN value"""
        if self.status:
            if self.channel <= self.MIN_CHANNEL:
                self.channel = self.MAX_CHANNEL
            else:
                self.channel -= 1

    def volume_up(self):
        """Increase the volume of the TV when TV is ON and does not exceed MAX value"""
        if self.status:
            self.muted = False
            if self.volume >= self.MAX_VOLUME:
                self.volume = self.MAX_VOLUME
            else:
                self.volume += 1


    def volume_down(self):
        """Decrease the volume of the TV when TV is ON and does not exceed MIN value"""
        if self.status:
            self.muted = False
            if self.volume <= self.MIN_VOLUME:
                self.volume = self.MIN_VOLUME
            else:
                self.volume -= 1


    def __str__(self) -> str:
        """Print TV status when muted and not muted"""
        if self.muted:
            return f'Power = {self.status}, Channel = {self.channel}, Volume = {self.MIN_VOLUME}'
        else:
            return f'Power = {self.status}, Channel = {self.channel}, Volume = {self.volume}'