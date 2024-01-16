class SmartSpeaker:
    def __init__(self, name, max_volume):
        self.name = name
        self.max_volume = max_volume
        self.connected_device = None

    def connect(self, other_speaker):
        self.connected_device = other_speaker

    def get_max_volume_of_connected_device(self):
        if self.connected_device:
            return self.connected_device.max_volume
        else:
            return 0

speaker1 = SmartSpeaker("Speaker 1", 70)
speaker2 = SmartSpeaker("Speaker 2", 80)

speaker1.connect(speaker2)

max_volume_of_connected_speaker = speaker1.get_max_volume_of_connected_device()
print(f"Max volume of connected speaker: {max_volume_of_connected_speaker}")

speaker1.connected_device = None