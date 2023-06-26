<h1>Test Run Setup</h1>

## Set Up the Test Run Configuration

1. Open PyCharm
2. In the navbar, select "Run" > "Edit Configurations..."
3. In the left pane, tap "+" button to create a new configuration
4. Select "Python tests" > "unittest"
5. Give the configuration a name (such as "SampleTestPlan")
6. In the right pane, under "Target" select either "Module name" or "Script Path" to target the test function
7. Enter the module name or script path (ex module: "test.application.newsreader.android.sample_test")
8. In the right pane, under "Environment", for "Environment variables:", click the ]file[ button on the right side of the entry box.
9. Click the "+" button to add a new key/value field, for each of the following variables:
   * "USER" = <your local machine's username (which should be <first_and_last_name>, like 'neilnorton')>
   * "APP" = "Newsreader"
   * "PLATFORM" = "Android"
   * "DEVICE" = <one of the device names from your JSON user profile list (ex: "Pixel 5")
10. Tap "Apply" in the bottom of the prompt, followed by "OK".
11. You should now be able to select that Run configuration from the Runtime selection, and Run or Debug Run a test

![](../../../../../../../../../var/folders/t7/6z4zpl6s4qx1kc6bhq6_3c980000gp/T/com.skitch.skitch/DMD3E089EE7-7572-4578-A59F-97A5B3F6D663/Run_Debug_Configurations.png)