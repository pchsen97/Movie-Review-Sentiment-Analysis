# Movie-Review-Sentiment-Analysis
DESIGN AND ANALYSIS OF ALGORITHM LAB PROJECT
SUBJECT:MOVIE REVIEW SENTIMENT ANALYSIS

DATASET: The dataset has been collected form https://xxx.lanl.gov/abs/cs/0409058 (A Sentimental Education:Sentiment Analysis using Subjectivity Summerization Based on minimum cuts )where the reviews with negative and positive sentiment respectively are stored in different folders and each review is in text form.The text file has been preprocessed to produce bag of words model and further analyzed.

METHOD: The text reviews has been preprocessed and bag of word model for each of positive and negative reviews has been made. Then word count is taken and words only with frequency greater  than 5 has been considered. A list with common words has been made containing those words falling under both negative and positive BOW models. Another list is made containing the probability of those common words of being in positive set and negative set.
Now to check sentiment of a new sample, first it is processed and then each word is checked. Two variables are taken to check positive and negative sentiments. If they are from negative list, increment the variable checking negative sentiments and do same for positive. If they fall under common category calculate the probability of their being positive and negative and multiply them with their count in the sample and add those results in those variables earlier mentioned. Ultimately the variable containing higher value will decide the sentiment of the review.
 
***Another procedure is also taken where the whole work has been done with Bernoulli Naïve Bayes using sklearn package with 81% accuracy[test size:0.2 train size:0.8] 

