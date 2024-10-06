const { Builder, By, Key, until } = require('selenium-webdriver');
const chrome = require('selenium-webdriver/chrome');
const proxyMiddleware = require('http-proxy-middleware');

// Set up ProxyMesh
const PROXY_URL = 'http://your-proxy-url.com:8080';
const proxyOptions = {
  proxyUrl: PROXY_URL,
  proxyAuth: { username: 'your-proxy-username', password: 'your-proxy-password' }
};

// Create a Chrome driver with ProxyMesh
const driver = new Builder()
 .forBrowser('chrome')
 .setChromeOptions(new chrome.Options().addArguments(['--headless']))
 .setProxy(proxyMiddleware(proxyOptions))
 .build();

// Navigate to the Twitter homepage
driver.get('https://twitter.com/');

// Wait for the page to load
driver.wait(until.elementLocated(By.css('[data-testid="trends"]')), 10000);

// Extract the top 5 trending topics
const topics = [];
const trendingTopics = driver.findElements(By.css('[data-testid="trend"]'));
for (let i = 0; i < Math.min(5, trendingTopics.length); i++) {
  const topic =  trendingTopics[i].findElement(By.css('a')).getText();
  topics.push(topic);
}

// Print the top 5 trending topics
console.log(topics);

// Close the driver
driver.quit();