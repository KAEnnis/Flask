"""
The US federal personal income tax is calculated based on the filing status 
and taxable income. 
Suppose we look at just one filing status: 
    single filers 
Example tax rates for are shown below.
+----------------------+-----------------------+---------------------------------+
| Taxable Income Range | Single Filer Rate (%) | Married Filing Jointly Rate (%) |
+----------------------+-----------------------+---------------------------------+
| $0 - $9,950          | 10                    | 10                              |
| $9,951 - $40,525     | 12                    | 12                              |
| $40,526 - $86,375    | 22                    | 22                              |
| $86,376 - $164,925   | 24                    | 24                              |
| $164,926 - $209,425  | 32                    | 32                              |
| $209,426 - $523,600  | 35                    | 35                              |
| Over $523,600        | 37                    | 37                              |
+----------------------+-----------------------+---------------------------------+

Write a program to ask a user a series of 
questions taking in their details and 
using the data from the above table, 
show their tax breakdown (% rate)

Ignore other tax details from the real-world for now

"""