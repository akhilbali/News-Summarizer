# News-Summarizer

<h3>Description</h3>
<p>News Summarizer is a web application that can provide automatic summarization of news articles.It works by providing the url of the news article(Currently, the application supports only urls from the New York Times website only).</p>

<h3>Requirements</h3>
1. python3</br>
2. Natural Language Toolkit(NLTK)</br>
3. Django</br>
4. BeautifulSoup</br>

<h3>How to run</h3>
<p>To start the server, you need to execute the command "python3 manage.py runserver" inside the summarizer directory which contains the manage.py file. Then go to your localhost "https://localhost:8000/home" and enter the url of the news article there.The system supports only News York Times' urls only.In order to use the application for some other news web-site, make necessary changes in the summarizer/web/extract.py.</p>

<h3>Application Details</h3>
<p>The application performs the extraction based summarization of the news article. Extractive summarization implies that the summary can be constructed by simply extracting the relevant sentences from the given document. The sentences are ranked in the document and the most relevant sentences are chosen in a non-redundant manner. </p>
<p>The technique used for performing summarization task is <a       href="https://web.eecs.umich.edu/~mihalcea/papers/mihalcea.emnlp04.pdf">TextRank</a>. TextRank is a graph-based ranking model for text processing. The text is considered as a graph with the sentences in the text representing the vertices of the graph.There is a concept of "similarity",which defines how a sentence relates to another sentence in the given text.This similarity is useful for calculating the rank of the sentences using the TextRank model.</p>
<p>In this implementation of TextRank, Cosine-Similarity has been used as the measure of "similarity" between the sentences.Cosine-Similarity is calculated using the Tf-Idf(term frequency-Inverse document frequency).For calculating the Inverse document frequency here, reuters corpus has been used from the NTLK library.</p> 
