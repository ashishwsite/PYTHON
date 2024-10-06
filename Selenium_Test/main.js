const { Builder, By, until } = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');

(async function getTwitterTrends() {
    // Set up Chrome options
    let options = new chrome.Options();
    // options.addArguments("--headless"); // Run in headless mode
    options.addArguments("--disable-gpu");
    options.addArguments("--no-sandbox");

    // Create a new instance of the Chrome driver
    let driver = await new Builder()
        .forBrowser('chrome')
        .setChromeOptions(options)
        .build();

    try {
        // Open Twitter home page
        console.log("try start")
       const data= await driver.get('https://twitter.com/home');

        // Add a delay to allow page to load (adjust as necessary)
        await driver.sleep(5000);

        console.log("data",data)
        // Locate the "What’s Happening" section
        // let trendingSection = await driver.wait(until.elementLocated(By.xpath('//section[contains(@aria-labelledby, "accessible-list-")]/div/div')), 10000);
  console.log("runtill 25 line ")
        // Fetch the top 5 trending topics
        // let trendingTopics = await trendingSection.findElements(By.xpath('.//div[@data-testid="trend"]'));
        // trendingTopics = trendingTopics.slice(0, 5); // Get only the top 5

        // Extract and print the trending topics
        // for (let i = 0; i < trendingTopics.length; i++) {
        //     let topic = trendingTopics[i];
        //     let trendName = await topic.findElement(By.xpath('.//span')).getText();
        //     console.log(`${i + 1}. ${trendName}`);
        // }
    } catch (e) {
        console.error('An error occurred:', e);
    } finally {
        // Close the driver
        await driver.quit();
    }
})();
