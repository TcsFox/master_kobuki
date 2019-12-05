#!/usr/bin/env node

/************************************************************************
 Copyright (c) 2017, Rethink Robotics
 Copyright (c) 2017, Ian McMahon

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.
************************************************************************/

'use strict';
/**
 * This example demonstrates simple sending of messages over the ROS system.
 */

// Require rosnodejs itself
const rosnodejs = require('rosnodejs');
// Requires the std_msgs message package
const std_msgs = rosnodejs.require('std_msgs').msg;
const bleno = require('bleno');


function initBLE() {
  console.log("we gte here");
  bleno.on('stateChange', function(state) {
    rosnodejs.log.info('on -> statechange: ' + state);
    if (state === 'poweredOn') {

      var buf = Buffer.alloc(31)

      bleno.startAdvertisingWithEIRData(buf)
    } else {
      bleno.stopAdvertising();
    }
  });

  bleno.on('advertisingStart', function(error) {
    rosnodejs.log.info('on -> advertisingStart: ' + (error ? 'error ' + error : 'success'));

  });
}

if (require.main === module) {
  // Invoke Main Talker Function
  initBLE();
}
