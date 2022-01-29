import random
import pandas as pd
import networkx as nx
from collections import defaultdict 
import json

class Similarity_Model:
	
	#K is a threshold such that if similarity between nodes is above K they will be connected
	#Weights is a vector of weights such that they sum to one
	def __init__(self, K=None, weights=None):
		#Sets K with some logical checks
		if(K is not None):
			if(K <= 0 or K >= 1):
				print("Threshold not in [0, 1]")
				exit()
			self.threshold = K
		else:
			self.threshold = random.random()
		
		#Sets weights with some logical checks
		if(weights is not None):
			if(sum(weights) - 1 < 0.01):
				self.weights = weights
			else:
				print("weights not normalized or weights not of correct length")
				exit()
		else:
			#Features 
			rand_weights = [1 for i in range(10000)]
			self.weights = [float(i)/sum(rand_weights) for i in rand_weights]
		
		#Setting our generated graph as an empty network graph
		self.generated_graph = nx.Graph()
		
		##### Getting the training graph
		PATH_TO_TRAINING_GRAPH = '../training_graph.csv'
		self.training_graph = self.get_training_graph(PATH_TO_TRAINING_GRAPH)
		
		#Mapping for Page Type
		df_classes = pd.read_csv('../node_classification.csv')
		self.page_mapping = dict(zip(df_classes.id, df_classes.page_type))
		
		##Getting JSON File
		with open('../node_features_text.json', 'r') as f:
			self.feature_mapping = json.load(f)
		
		"""
		VARIABLES:
		THRESHOLD
		WEIGHTS
		GENERATED_GRAPH
		TRAINING_GRAPH
		PAGE_MAPPING
		FEATURE_MAPPING
		"""
		
	#Reads the training graph from a file
	def get_training_graph(self, graph_file_name):
		df = pd.read_csv(graph_file_name)
		G = nx.from_pandas_edgelist(df, source = 'node1', target = 'node2')
		return G
	
	
	#Calcualte Similarity
	def similarity_metric(self, node1, node2):
		similarity_sum = 0#self.weights[0] * int(self.page_mapping[node1] == self.page_mapping[node2])
		
		feature_set1 = set(self.feature_mapping[str(node1)])
		feature_set2 = set(self.feature_mapping[str(node2)])
		intersection_set = feature_set1.intersection(feature_set2)
		similarity_sum += sum([self.weights[i] for i in intersection_set])
		
		return similarity_sum
	
	def create_generated_graph():
		nodes = self.training_graph.nodes()
		for i in nodes:
			for j in nodes:
				if(i != j and similarity_metric(i, j) > K):
					self.generated_graph.add_edge(i, j)
					
	def error(self):
		####TODO MAKE ERROR FUNCTION FUUUUUUCK
		return "FUCK YOU"
		

G = Similarity_Model()
for i in range(10000):
	num = G.similarity_metric(8299, i)
	if(num > 0):
		print(i, num)

