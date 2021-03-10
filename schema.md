## Schema: The information about the structure of the database and how things relate to each other

## Background

# Before storing our data we must design a schema for it so that we can create it in our database.

### User Story

> **As a** product owner
> **I want to** agree on the design of the schema
> **So that** the data is easy to query


## Table: Isle of Wight sales data

order_id|date_time |product_ids|order_amount|payment_method|
        |          |           |            |              |
        |          |           |            |              |
        |          |           |            |              |
        |          |           |            |              |


## Table: Products

product_id|product_name|product_size_id|product_price|
          |            |               |             |
          |            |               |             |
          |            |               |             |

## Table: Products size

id|product_size|
1 |small       | 
2 |medium      |
3 |large       |
4 |standard    |

## Table: PII

customer_id|first_name|last_name|


## Table: Payment method

id|payment_type
1 | cash
2 | card


