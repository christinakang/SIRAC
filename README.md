## SIRAC:  semi-structured IRAC(Issue, Rule, Application and Conclusion) corpus for legal scenarios
SIRAC :  semi-structured IRAC(Issue, Rule, Application and Conclusion) corpus for legal scenarios

This repository contains the code for the SIRAC ： semi-structured IRAC(Issue, Rule, Application and Conclusion) corpus for legal scenarios. The project is associated paper "Can ChatGPT Perform Reasoning Using the IRAC Method in Analyzing Legal Scenarios Like a Lawyer?". The data orpus conssiting of scenarios pertain to Contract Acts Malaysia and Australian Social Act for Dependent Child. 

IRAC (Issue, Rule, Application and Conclusion) is framework widely used by legal professionals for organizing legal analysis. Each scenarios in the corpus is annotated with a complete IRAC analysis in a semi-structred format so that both machines and legal professionals are albe to interpret and nderstand the annotations. 


In addition, we conduct the first empirical assessment of ChatGPT for IRAC analysis in order to understand how well they align with the analysis of legal professionals. Our experimental results shed lights on possible future research directions to improve alignments between LLMs and legal experts in terms of legal reasoning. 


## Quickstart

1. Install the package from github.

``` python
   pip install git+https://github.com/christinakang/SIRAC.git
```

2. Load the scenario 

The annotated data corpus is avaialbe [here](https://github.com/christinakang/SIRAC/blob/main/data/scenario.json)

``` python
   python ./script/readScenario.py
```

## Dataset File Structure 

``` 
   {
            "id": "s01",
            "type": "Contract Law",
            "scenario": "Alan needed money quickly. He owned an original 1886 edition of Kidnapped by Robert Louis Stevenson, a book which he advertised in the newspaper for sale for $1000. Cate saw the advertisement. She telephoned Alan, saying that she would buy the book for $1000. Alan, however, replied that he had reconsidered the matter and that he could not sell the book for less than $2000.Cate replied that she would give him $1500. Alan replied that he would only sell the book for $2000 but that he would keep his offer open for seven days.He also said that Cate could fax her acceptance to him if she wanted.The next day Alan sold the book to his friend David because David loved the book so much and because he paid $7000 for it. Two days later Cate decided to purchase the book for Alan's price of $2000.She posted her acceptance to Alan.The next day David told Cate that he had bought a copy of Kidnapped from Alan for $7, 000. Cate rang Alan to confirm that she had accepted his offer.Later that day Alan received Cate's acceptance.",
            "issue": "whether there is a valid contract between Alan and Cate",
            "dceompose question": "1. Was the advertisement put out by Alan an invitation to treat or an offer\n2.  Whether Alan has accepted Cate's offer to buy the book at 1000\n3. Whether Alan is bound to keep his offer open for 7 days\n4. Whether there is valid acceptance by Cate for Alan's offer to sell at 2000\n",
            "analysis": "(1) According to {Eckhardt Marine GmbH v Sheriff, High Court of Malaya, Seremban (2001) 4 MLJ 49[]} THEN Alan's advertisement to sell the book for $1000 is an invitation to treat {LEGALLIZATION}\n(2) IF Alan's advertisement to sell the book for $1000 is an invitation to treat THEN Cate's reply to buy the book for $ 1000 is an offer. {Section 4.1} {LEGALLIZATION}\n(3) Alan's reply saying that he could not sell the book for less than $2000 is not an acceptance because acceptance must be absolute and unqualified.{Section 7a} {LEGALLIZATION} {AND} since Alan changed the price from $1500 to $2000, he made a counter offer which in effect destroyed Cate's original offer {Malayan Flour Mills Bhd v Saw Eng Chee (Administrator of the estate of Saw Cheng Chor, decd) (1997) 1 MLJ 763. []}{LEGALLIZATION}\n(4) Cate's reply to buy at $1500 is also a counter offer {CO-REFERENCE (3)}\n(5) Alan did not accept Cate's counter offer but he made another counter offer that he would only sell the book for $2000 {AND} he would keep his offer open for seven days.[TKN1]  {CO-REFERENCE(3)}\n(6) IF acceptance is made by post THEN it takes effect upon posting  {Adams v Lindsell (1818) 1 B & Ald 681[]} {LEGALLIZATION}\n(7) {HOWEVER} Alan's offer has a specification of mode of offer therefore postal rule does not apply {AND} Cate's acceptance is invalid {Section 7b} {LEGALLIZATION}\n(8) IF Cate's acceptance is not valid THEN Alan can revoke his offer {Section 5.1}{LEGALLIZATION}\n(9) {HOWEVER} revocation only takes effect when it is communicated to Cate {Section 6a} {LEGALLIZATION}\n(10) ACCORDING TO {Section 6a}, revocation has to be made by the offeror, IF revocation has been communicated by David who is a third party THEN revocation is invalid.\n(11) IF revocation invalid THEN Cate can still accept the offer. \n(12) SINCE Cate has rang Alan to confirm her acceptance THEN her acceptance is communicated. {Section 2}\n(13) IF (12) THEN there is a valid contract between Alan and Cate \n",
            "conclusion": "yes, there is a valid contract between Alan and Cate"
        },
  ```
## Statics of the data 

|           | Scenarios | Issues | Rules | Average Length of reasoning 
|-----------|-----------|--------|-------|-----------------------------|
| SIRAC_ASA | 30        | 1      | 3     | 4.8                         |
| SIRAC_CAM | 20        | 20     | 55    | 9.3                         |
| SIRAC     | 50        | 21     | 58    | 7.05                        |





## Experiment

The experiment set up is saved in the ``` ./script/experimentsPrompt.py ```

## Extra data 

If you need the evaluation matrix result from each experiment, you can email xiaoxi.kang@monash.edu for more information. 

## Citation

If you find this useful in your research, please consider citing :
```
@inproceedings{
anonymous2023can,
title={Can Chat{GPT} Perform Reasoning Using the {IRAC} Method in Analyzing Legal Scenarios Like a Lawyer?},
author={Anonymous},
booktitle={The 2023 Conference on Empirical Methods in Natural Language Processing},
year={2023},
url={https://openreview.net/forum?id=7okuG5JhaM}
}
```
