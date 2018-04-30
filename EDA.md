# Exploratory Data Analysis

## DataSet1

1 record where CurrentStatus is "Moved In", but NotQual is "Not Age Qualified", although DeactDate is unpopulated and DeactReason is unpopulated

1 record where ProjectedMoveIn is populated, but CurrentStatus is "Deactivated", DeactDate is populated, and DeactReason is "Not Qualified"

1 record where DeactDate is "2/24/2105"
1 record where DeactDate is "2/16/3014"
1 record where DeactDate is "4/1/3015"
1 record where DeactDate is "11/28/2018 6:00", but ProjectedMoveIn is "3/5/2017 20:31"

## DataSet2

## DataSet3

64 records where istatus is "current", but 'dtmoveout' is populated

## DataSet4

2 records where Amount is negative

## Data Preparation/Treatment

    DataSet1
        Ageatinquiry
            NULL < 21 (lowest age with “Not Age Qualified”)
            NULL > 116
            Impute Mean 82 (~81.76)
        DeactDate
            ds13[ds13.DeactDate == "3015-04-01 05:00:00"] = "2015-04-01 05:00:00"
            ds13[ds13.DeactDate == "3014-02-16 06:00:00"] = "2014-02-16 06:00:00"
            ds13[ds13.DeactDate == "2105-02-24 05:00:00"] = "2015-02-24 05:00:00"
            ds13[ds13.DeactDate == "2019-03-30 04:00:00"] = "2018-03-30 04:00:00"
            ds13[ds13.DeactDate == "2018-11-28 06:00:00"] = "2017-11-28 06:00:00"
    DataSet3
        istatus
            = "Moved Out", where dtmoveout <> ""
    DataSet4
        Amount
            * -1, where < 0
