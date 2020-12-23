class KNN:
	K = None

	x_data = None
	y_data = None

	def __init__(self, K: int):
		self.K = K

	def fit(self, x_data, y_data) -> None:
		"""sets the train data"""
		self.x_data = x_data
		self.y_data = y_data

	def predict(self, test_x : list) -> list:
		""" returns the list of prediction for a list of data"""
		return [self.__KNNAlgorithm(test_data) for test_data in test_x]

	def set_K(self, K : int) -> None:
		self.K = K

	def __KNNAlgorithm(self, data):
		"""KNN algorithm for a single value"""

		# get the list of distances to other values
		distance_list = self.__get_distance_list(data)
		
		# take the classes of the closest k neighbors
		closest_k_classes = [distance_list[i][1] for i in range(self.K)]

		return self.__find_most_frequent(closest_k_classes)

	def __get_distance_list(self, data) -> list:
		""" returns the sorted list of distances to each data in train list.
			the format is [(distance1, class1), (distance2, class2),...]
		"""
		i = 0

		size = len(self.x_data)
		distance_list = []

		while i < size:
			distance = self.__ecludian_distance(data, self.x_data[i])
			distance_list.append((distance, self.y_data[i]))
			i += 1

		distance_list = sorted(distance_list)
		return distance_list

	@staticmethod
	def __find_most_frequent(values : list):
		"""returns the most frequent value in a list"""
		max_count = 0
		max_value = None

		for i in values: 
			if values.count(i) >= max_count:
				max_count = values.count(i)
				max_value = i

		return max_value

	@staticmethod
	def __ecludian_distance(point1 : list, point2 : list) -> float:
		"""calculates the distance between any two points in any dimension"""
		distance_sqr = 0
		i = 0
		
		size = len(point1)

		while i < size:
			distance_sqr += (point2[i] - point1[i]) * (point2[i] - point1[i])
			i += 1

		return distance_sqr

