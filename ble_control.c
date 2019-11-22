#include <stdbool.h>
#include <stdint.h>

#include "simple_ble.h"



// Intervals for advertising and connections
static simple_ble_config_t ble_config = {
        // c0:98:e5:49:xx:xx
        .platform_id       = 0x49,    // used as 4th octect in device BLE address
        .device_id         = 0x0006,  // TODO: replace with your lab bench number
        .adv_name          = "HOPE", // Note that this name is not displayed to save room in the advertisement for data.
        .adv_interval      = MSEC_TO_UNITS(1000, UNIT_0_625_MS),
        .min_conn_interval = MSEC_TO_UNITS(500, UNIT_1_25_MS),
        .max_conn_interval = MSEC_TO_UNITS(1000, UNIT_1_25_MS),
};


/*******************************************************************************
 *   State for this application
 ******************************************************************************/
// Main application state
simple_ble_app_t* simple_ble_app;

int main(void) {

  // Setup BLE
  simple_ble_app = simple_ble_init(&ble_config);

  simple_ble_adv_only_name();


  while(1) {
	sleep(1);
  }
}
