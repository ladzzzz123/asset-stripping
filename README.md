# Asset Stripping
A simple example of an asset stripping problem fund managers at private equity companies face.

### Problem Description
Large private equity firms make money from purchasing and re-selling companies, a process sometimes known as **"asset stripping"**. They do this by purchasing sufficient shares in public companies to gain outright ownership of the companies, making them private. They then make internal changes to the companies before offering them for re-sale at a profit. Fund Managers are employed by private equity firms to buy and sell companies in such a way as to maximise the return on investment.

At any particular time, Fund Managers will have funds at their disposal for investment in public companies whose stock is traded on global investment markets. They face a complex task in deciding what companies to purchase given the funds available. The amount of funds available constrains the total cost of all the companies purchased. Fund Managers therefore have to decide which companies to purchase from the market. There are a number of criteria that apply:

*   Each company will require a certain investment to buy enough shares to take control of the company. The total investment in companies may not exceed the available investment funds.
*   Each company has a value to the private equity firm based on an estimate of the return on investment that can be realised when the company is re-sold. The Fund Manager must attempt to maximise the realisable return on investment from companies purchased and re-sold.
* Certain companies, though independent of each other, have compatible businesses. Greater value can often be obtained by purchasing a group of compatible companies that can then be merged to produce a stronger, and more valuable, company. There is therefore a bonus return on investment if a group of compatible companies are purchased together.

Decide which companies to purchase for a private equity firm with available funds. The supplied file **companies.txt** contains details of 100 companies currently being considered for purchase by Jonathan & Bramble AssetStrippers Ltd., a large private equity company. The information is set out in the following format:

- *funds available*: the first line contains the overall funds, in units of £1M, available for stock purchase, in this case £2,000,000,000.
- *investments*:  the investment required to obtain each stock, in units of £1M, is given in order as a comma-separated list. The total investment required to purchase all companies is £3,851,000,000. This is obviously more than the funds available
- *realisable returns*: the realisable return on investment, in units of £1M, for each company is given in order as a comma-separated list
- *linked groups*: each group of compatible companies is described giving the list of the companies in the group, identified by their position in the list of companies, in a comma-separated form followed by a space followed by the bonus value that can be realised if all the companies are purchased together. For example, the first group consists of the companies at positions 0, 1, 2 and 3 in the list of companies. There are three such groups with bonuses £80,000,000, £100,000,000 and £200,000,000 respectively available if all companies in the group are purchased.

### Note
To run the program, you need to install [pyeasyga](https://github.com/remiomosowon/pyeasyga). Then run:

```python
    python asset_stripping.py
```

### Example Output
63 Selected Companies: [1, 2, 3, 4, 5, 6, 7, 12, 15, 16, 17, 18, 19, 20, 21, 22, 24, 25, 27, 28, 30, 32, 33, 34, 35, 37, 40, 41, 43, 44, 46, 48, 50, 51, 53, 55, 57, 58, 59, 63, 66, 67, 69, 72, 73, 74, 76, 77, 79, 80, 81, 82, 83, 89, 90, 91, 92, 94, 95, 96, 98, 99, 100]
Total Investment: 1999
Total Value: 3830
