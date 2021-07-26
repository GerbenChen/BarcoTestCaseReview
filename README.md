# Barco TestCase Warranty Info
> Using **Selenium** combine with **Unittest** to design Test Case for warranty-info on Barco Website

## Test strategy
> Project data collection
>> Collect information from database

> Quality goals
>> Ensure data accuracy, user experience, and performance usage, avoid serious exception.

> Test category
>> Including Unit testing, Interface testing, Regression testing, Performance Testing, Load testing, Security testing, Compatibility testing, Usability testing.

> Test tools and framework
>> selenium, unittest

> Test phase
>> Unit Testing, Integrated Testing, System Testing, Stress Testing

> Test Metrics
>> Pass condition : No high severity bug.

> Risk analysis
>> I think the serial number must limit can not type special character to avoid special situation.
>> If User's environment is more complicated, maybe will make deviation.

> Continuous improvement
>> In futures, I will create API to test, it can check BackEnd and Database, and how performance about run time, data accuracy and have any omissions from FrontEnd.
>> I will using Sikuli to test performance about numbers of connections, elements offset on windows, it also can accurated positioning and check image is correct or not.  


## Requirement
* Python 3.x+
* pip install selenium
* pip install xmlrunner
* Refer to your browser version to download Gecko or Chrome or others driver.

## Test Case Structure
![warranty (1)](https://user-images.githubusercontent.com/61812113/126738730-46be7845-1971-4bb8-90b1-2af802ab6e23.jpg)

- [x] 1. Type Correct Serial Number to enter Correct Page
- [x] 2. Special Character
- [x] 3. Minimum 6 Characters Required
- [x] 4. Type Wrong Will Display Error Message
- [x] 5. Screen Resolution
- [x] 6. How Many Response Times About Get Info
- [ ] 7. How Many Users Can Use at the Same Times
- [x] 8. Open Page On Different Browser. Ex: Windows/Firefox/MacOS
- [x] 9. Click Get Info Can Get Information or Not
- [x] 10. Click Read Our Warranty Policy Turn to Correct Page or Not
- [x] 11. If I Type Any Wrong Serial Number Have Possible to Get Correct Infomation or NOT 

## Command Line
> python3 <directory> warrantyinfo_testcase.py -v(-v will see more details)
  
# Docker
* Using Ubuntu 18.04 and Run python on Docker
  
## DockerFile
> Please Check and modify DockerFile content
  
# Jenkins
* Using pipeline on Jenkins
  
## JenkinsFlie
> Please Check and modify JenkinsFlie content 
  
