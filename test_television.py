import unittest

from week13.television import Television


class TestTelevision(unittest.TestCase):
    def test_init(self):
        tv = Television()
        self.assertEqual(tv.__str__(), "Power = False, Channel = 0, Volume = 0")

    def test_power(self):
        tv = Television()

        #power on
        tv.power()
        self.assertEqual(tv.__str__(), "Power = True, Channel = 0, Volume = 0")

        #power off
        tv.power()
        self.assertEqual(tv.__str__(), "Power = False, Channel = 0, Volume = 0")

    def test_mute(self):
        tv = Television()
        tv.power()

        #power on and volume increased once and muted
        tv.volume_up()
        tv.mute()
        self.assertEqual(tv.__str__(), "Power = True, Channel = 0, Volume = 0")

        #power on and unmuted
        tv.mute()
        self.assertEqual(tv.__str__(), "Power = True, Channel = 0, Volume = 1")

        #power off and muted
        tv.power()
        tv.mute()
        self.assertEqual(tv.__str__(), "Power = False, Channel = 0, Volume = 1")

        #power off and unmuted
        tv.mute()
        self.assertEqual(tv.__str__(), "Power = False, Channel = 0, Volume = 1")

    def test_channel_up(self):
        tv = Television()

        #increase channel with power off
        tv.channel_up()
        self.assertEqual(tv.__str__(), "Power = False, Channel = 0, Volume = 0")

        #increase channel with power on
        tv.power()
        tv.channel_up()
        self.assertEqual(tv.__str__(), "Power = True, Channel = 1, Volume = 0")

        #power on and exceed max channel
        tv.channel_up()
        tv.channel_up()
        tv.channel_up()
        self.assertEqual(tv.__str__(), "Power = True, Channel = 0, Volume = 0")

    def test_channel_down(self):
        tv = Television()

        #decrease channel with power off
        tv.channel_down()
        self.assertEqual(tv.__str__(), "Power = False, Channel = 0, Volume = 0")

        #power on and channel exceeds min val
        tv.power()
        tv.channel_down()
        self.assertEqual(tv.__str__(), "Power = True, Channel = 3, Volume = 0")

        #decrease channel with power on
        tv.channel_down()
        self.assertEqual(tv.__str__(), "Power = True, Channel = 2, Volume = 0")

    def test_volume_up(self):
        tv = Television()

        #power off and volume increase
        tv.volume_up()
        self.assertEqual(tv.__str__(), "Power = False, Channel = 0, Volume = 0")

        #power on and volume increased
        tv.power()
        tv.volume_up()
        self.assertEqual(tv.__str__(), "Power = True, Channel = 0, Volume = 1")

        #power on, tv is muted, and volume increased
        tv.mute()
        tv.volume_up()
        self.assertEqual(tv.__str__(), "Power = True, Channel = 0, Volume = 2")

        #power on and volume exceeds MAX val
        tv.volume_up()
        self.assertEqual(tv.__str__(), "Power = True, Channel = 0, Volume = 2")

    def test_volume_down(self):
        tv = Television()

        #power off and decrease volume
        tv.volume_down()
        self.assertEqual(tv.__str__(), "Power = False, Channel = 0, Volume = 0")

        #power on and volume decreased from max
        tv.power()
        tv.volume_up()
        tv.volume_up()
        tv.volume_down()
        self.assertEqual(tv.__str__(), "Power = True, Channel = 0, Volume = 1")

        #power on, muted, and decrease volume
        tv.mute()
        tv.volume_down()
        self.assertEqual(tv.__str__(), "Power = True, Channel = 0, Volume = 0")

        #power on, unmuted, volume deceased exceeding MIN val
        tv.mute()
        tv.volume_down()
        tv.volume_down()
        tv.volume_down()
        self.assertEqual(tv.__str__(), "Power = True, Channel = 0, Volume = 0")