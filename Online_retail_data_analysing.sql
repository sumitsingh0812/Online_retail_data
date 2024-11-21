SELECT * FROM orders.`power bi dataset`;
SELECT * FROM orders.`power bi dataset` order by profit desc;
SELECT * FROM orders.`power bi dataset` ORDER BY sales DESC;
select*from orders.`power bi dataset` order by quantity desc;
select max(sales) from orders.`power bi dataset`;
select max(profit) from orders.`power bi dataset`;

-- Sales Performance:

-- What are the total sales and profits for each category and sub-category?
SELECT Category, SUM(Sales) AS Total_Sales, SUM(Profit) AS Total_Profit
FROM orders.`power bi dataset`
GROUP BY Category;

-- Which product has the highest total sales?
select `Product Name`,sum(sales) as maxsale
 FROM orders.`power bi dataset`
 group by `Product Name`
 order by maxsale desc;
 
-- What are the top 5 products by sales and profit?
select `product name`,sum(sales) as ss, sum(profit) as sp
from orders.`power bi dataset`
group by `product name`
order by ss desc,sp desc;

-- Customer Insights:

-- What are the total sales and profits by customer?
select `customer name`,sum(sales) as ss,sum(profit)as sp
from orders.`power bi dataset`
group by `customer name`
order by ss desc,sp desc;

-- Which customer has made the most purchases or has the highest total spend?
select `Customer Name`,max(quantity) as mq,max(sales)as ms
from orders.`power bi dataset`
group by `Customer Name`
order by mq desc, ms desc;

-- Geographical Analysis:

-- What are the total sales and profits by country, state, or region?
select `country`,`state`,`region`, max(sales) as ms, max(profit) as mp
from orders.`power bi dataset`
group by `country`,`state`,`region`
order by ms desc,mp desc;

-- Which city or region has the highest total sales?
select `region`,`city`,sum(sales) as ss
from orders.`power bi dataset`
group by `region`,`city`
order by ss desc
limit 3;

-- Temporal Trends:

-- How do sales and profits trend over time (e.g., monthly, quarterly)?
SELECT CONCAT(YEAR(STR_TO_DATE(`Order Date`, '%Y-%m-%d')), '-Q', QUARTER(STR_TO_DATE(`Order Date`, '%Y-%m-%d'))) AS Quarter, 
       SUM(Sales) AS Total_Sales, 
       SUM(Profit) AS Total_Profit
FROM orders.`power bi dataset`
GROUP BY Quarter
ORDER BY Quarter;

-- Are there any seasonal patterns in sales or profits?
SELECT 
    YEAR(STR_TO_DATE(`Order Date`, '%Y-%m-%d')) AS Year, 
    MONTH(STR_TO_DATE(`Order Date`, '%Y-%m-%d')) AS Month, 
    SUM(Sales) AS Total_Sales, 
    SUM(Profit) AS Total_Profit
FROM orders.`power bi dataset`
GROUP BY Year, Month
ORDER BY Year, Month;

-- Order Analysis:

-- What is the average order value?


select `Customer Name`,sum(sales) as ss
FROM orders.`power bi dataset`
group by `customer name`
order by ss desc
limit 10;

-- What are the total quantities ordered by category or product?
select `category`,`product name`,sum(quantity) as sq
FROM orders.`power bi dataset`
group by `category`,`product name`
order by sq desc
limit 10;

-- How does the cost and selling price compare across different segments?
SELECT segment, sum(sales) as ss, sum(cost) as sc,
sum(sales)-sum(cost) as profit
FROM orders.`power bi dataset`
group by segment
order by profit desc;
SELECT 
    Segment, 
    SUM(Cost) AS Total_Cost, 
    SUM(Sales) AS Total_Sales, 
    SUM(Sales) - SUM(Cost) AS Profit, 
    AVG(Sales) AS Avg_Sales, 
    AVG(Cost) AS Avg_Cost, 
    AVG(Sales) - AVG(Cost) AS Avg_Profit
FROM orders.`power bi dataset`
GROUP BY Segment
ORDER BY Profit DESC;


-- Segmentation:

-- How do sales and profits differ by segment (e.g., consumer, corporate)?
SELECT 
    Segment, 
    SUM(Sales) AS Total_Sales, 
    SUM(Profit) AS Total_Profit,
    AVG(Sales) AS Avg_Sales_Per_Order,
    AVG(Profit) AS Avg_Profit_Per_Order
FROM orders.`power bi dataset`
GROUP BY Segment
ORDER BY Total_Sales DESC;

-- What are the sales and profit distributions across different ship modes?
select `ship mode`,sum(sales)  as totalsales,sum(profit) as totalprofit,AVG(Sales) AS Avg_Sales_Per_Order,
    AVG(Profit) AS Avg_Profit_Per_Order
FROM orders.`power bi dataset`
group by `ship mode`
order by totalsales;
#Profitability Analysis:

-- What is the average profit margin by category or sub-category?
select `category`,`sub-category`, avg(profit) as average_profit
FROM orders.`power bi dataset`
group by `category`,`sub-category`
order by average_profit desc;

-- Which category or sub-category has the highest profit margin?
select `category`,`sub-category`, max(profit) as average_profit
FROM orders.`power bi dataset`
group by `category`,`sub-category`
order by average_profit desc;
SELECT 
    Category, 
    SUM(Sales) AS Total_Sales, 
    SUM(Profit) AS Total_Profit,
    (SUM(Profit) / SUM(Sales)) * 100 AS Profit_Margin
FROM orders.`power bi dataset`
GROUP BY Category
ORDER BY Profit_Margin DESC
LIMIT 1;

-- Product Performance:

-- What are the sales trends for each product over time?
SELECT 
    `Product Name`, 
    DATE_FORMAT(STR_TO_DATE(`Order Date`, '%Y-%m-%d'), '%Y-%m') AS Month, 
    SUM(Sales) AS Total_Sales
FROM orders.`power bi dataset`
GROUP BY `Product Name`, Month
ORDER BY `Product Name`, Month;

-- How do different products compare in terms of profitability? --
SELECT 
    `Product Name`, 
    SUM(Sales) AS Total_Sales, 
    SUM(Profit) AS Total_Profit,
    (SUM(Profit) / SUM(Sales)) * 100 AS Profit_Margin
FROM orders.`power bi dataset`
GROUP BY `Product Name`
ORDER BY Profit_Margin DESC;

