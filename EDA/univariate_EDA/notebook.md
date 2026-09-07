## Univariate Analysis of Data (EDA)

### - Orders Dataset (Featured)

#### -> For Columns order_status, we can clearly see this, that almost 97% orders are delivered to customers, and appox 1.5 percent orders are shipped or in processing

```order_status Column```
```
delivered      97.020344
shipped         1.113223
canceled        0.628513
unavailable     0.612423
invoiced        0.315765
processing      0.302692
created         0.005028
approved        0.002011
Name: count, dtype: float64
```

#### -> For columns `is_delayed` , we can see that 93% orders were delivered on time, nd ~ 7% were delayed

``` is_delayed Column ```

```
is_delayed
0    92.129001
1     7.870999
```

#### -> Acc to column `is_repeat_customer`, 93 % customer are new to the store , and appox 7 % customers are repeat customers.

``` is_repeat_customer ```
```
is_repeat_customer
0    93.622349
1     6.377651
Name: count, dtype: float64
```