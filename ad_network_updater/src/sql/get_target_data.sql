select dt, network, currency, platform, cost as cost_target from {table_name}
where dt in ({dates}) 
and network in ({networks})
and currency in ({currencies})
and platform in ({platforms})