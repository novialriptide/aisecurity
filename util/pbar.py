import json
from termcolor import cprint


class ProgressBar:

    def __init__(self, logger, length=16, marker="#", ws=None):
        self.logger = logger
        self.bar_length = length - 2  # compensate for [] at beginning and end
        self.marker = marker
        self.progress = 0.
        self.blank = " " * self.bar_length
        self.ws = ws
        self.set_message("Initializing....")

    def set_message(self, message):
        if self.ws is not None:
            self.ws.send(json.dumps({"pbar": message}))
        else:
            cprint(message, attrs=["bold"])

    def reset(self, message=None):
        self.progress = 0.
        if message:
            self.set_message(f"{message}\n[{self.blank}]")

    def _update(self, amt, message):
        self.progress += amt / self.logger.frame_threshold
        num_done = int(round(min(1., self.progress) * self.bar_length))
        done = (self.marker * num_done + self.blank)[:self.bar_length]
        self.set_message(f"{message}\n[{done}]")
        if self.progress >= 1.:
            self.progress = 0.

    def update(self, face, rec, amt=1., message="Recognizing....."):
        if not rec:
            return False
        try:
            pts = face["keypoints"]
            eye_diff = abs(pts["right_eye"][0] - pts["left_eye"][0])
            x, y, w, h = face["box"]

            ratio = eye_diff / w
            looking = ratio > 0.4
            print(f"ratio: {ratio}")
            if looking:
                self._update(amt, message)
            return looking
        except TypeError:
            return False
