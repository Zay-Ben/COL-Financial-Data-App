# COL Financial Data App

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://col-financial.streamlit.app)

COL Financial, one of the largest stockbrokers in the Philippines, provides fundamental and technical data to investors and traders. However, the data are separated, with discrepancies in timing and limited variables, posing challenges for users to identify potential investments and trades.

This app addresses these challenges by:
1. Aggregating fundamental and technical data from multiple sources into a single source of truth.
2. Updating the data using the most recent information, addressing timing discrepancies.
- For example, the All Shares Index updates data in real-time, the Investment Guide updates data weekly, and the Technical Guide updates data daily. The decision to buy and sell a stock should happen in real-time to maximize opportunities and minimize risks.
4. Creating new variables from old variables, providing additional insights.
- Some investors would like to see a stock price with respect to its fair value to assess its valuation, while some traders would prefer to consider a stock's price relative to its 52-week high to gauge its strength.
5. Visualizing data to identify potential investments and trades, facilitating informed and timely decision-making

Please note that the app is not affiliated with COL Financial and has some limitations, such as the lack of historical and fundamental data for some stocks, as well as some data being estimated by analysts. Nonetheless, the app still provides valuable insights for investors and traders in the Philippine stock market.

![image](https://github.com/Zay-Ben/COL-Financial-Data-App/assets/101090718/617739b0-f223-48e6-bffe-b931fb32f4f7)

## Usage

Click here to watch [the COL Financial App Demonstration video](https://www.youtube.com/watch?v=dpicjW7MqEo).

To use the app, follow these simple steps:
1. Create an xlsx file.
2. In the file, create three sheets namely ASI, IG, and TG for All Shares Index, Investment Guide, and Technical Guide, respectively.
3. Copy and paste each data from the website of the stockbroker to its respective sheet.
4. Upload the file to the app.

Once the file has been uploaded, the app will then output a xlsx file containing the aggregated data, providing a comprehensive view of the stock market for investors and traders.

## License

[MIT](https://choosealicense.com/licenses/mit/)
