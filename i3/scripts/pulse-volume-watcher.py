#!/usr/bin/env python3
from pulsectl import Pulse, PulseLoopStop
import sys

# Adapt to your use-case
sink_id = 0

with Pulse() as pulse:
  default_sink_name = pulse.server_info().default_sink_name
  for sink in pulse.sink_list():
    if sink.name == default_sink_name:
      sink_id = sink.index
      break

  def callback(ev):
    if ev.index == sink_id:
        raise PulseLoopStop
  try:
    pulse.event_mask_set('sink')
    pulse.event_callback_set(callback)
    last_value = round(pulse.sink_list()[sink_id].volume.value_flat * 100)
    last_mute = pulse.sink_list()[sink_id].mute == 1
    while True:
      pulse.event_listen()
      value = round(pulse.sink_list()[sink_id].volume.value_flat * 100)
      mute = pulse.sink_list()[sink_id].mute == 1
      if value != last_value or mute != last_mute:
        print(value, end='')
        if mute:
            print('!')
        else:
            print('')
        last_value = value
        last_mute = mute
      sys.stdout.flush()
  except:
    pass
