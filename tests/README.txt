Add your own test cases here.

input:

    ```
    ['portable', 'long_battery', 'budget_medium', 'gaming', 'creative_work', 'office', 'pref_os_lin', 'large_screen', 'travel_often']
    ```

expected: 

    ```
    Midrange Gaming Laptop
    specs: 
        60wh+ battery
        16+ gigs of RAM
        large screen
        Linux supported HW
    ```

input: 

    ```
    ['portable', 'budget_low', 'gaming', 'creative_work', 'office', 'pref_os_lin', 'needs_ai_accel']
    ```

expected:

    ```
    Budget Ultrabook
    specs: 
        GPU with tensor cores
        16+ gigs of RAM
        Linux supported HW
    ```

input:

```
    ['portable', 'long_battery', 'budget_high', 'pref_os_lin']
```

expected:

    ```
    Premium Ultrabook
    specs: 
    ```