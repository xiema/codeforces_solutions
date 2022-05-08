require 'net/http'
require 'nokogiri'
require 'selenium-webdriver'

url = ARGV[0]

# resp = Net::HTTP.get(URI(url))
# driver = Selenium::WebDriver.for :firefox, options: Selenium::WebDriver::Firefox::Options.new(args: ['--headless'])
driver = Selenium::WebDriver.for :firefox, capabilities: Selenium::WebDriver::Firefox::Options.new(args: ['--headless'])
driver.get(url)
resp = driver.page_source

doc = Nokogiri::HTML.parse(resp)
problem = doc.xpath("//div[@class='problem-statement']")
title = problem.xpath("//div[@class='title']").children[0].text
title.gsub!(/[^\w]/, '')
if /problemset/ === url
  problemid = /problem\/(\w*)\/(\w*)/.match(url).captures.join
else
  problemid = /(\w*)\/problem\/(\w*)/.match(url).captures.join
end

sampleinput = doc.xpath("//div[@class='input']/pre").children.map {|c| c.text.lstrip}
sampleoutput = doc.xpath("//div[@class='output']/pre").children.map {|c| c.text.lstrip}

dirname = "#{File.dirname(__FILE__)}/solutions/#{problemid} #{title}"
Dir.mkdir(dirname) if !Dir.exist?(dirname)

testdirname = "#{dirname}/tests"
Dir.mkdir(testdirname) if !Dir.exist?(testdirname)
sampleinput.each_with_index do |intxt, i|
  outtxt = sampleoutput[i]
  File.open("#{testdirname}/sample#{i+1}.in", 'w') {|f| f.write(intxt)}
  File.open("#{testdirname}/sample#{i+1}.out", 'w') {|f| f.write(outtxt)}
end
