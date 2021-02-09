'''
Author: Connor Parish (cbp5nd@virginia.edu)
Contains class representing resting-state fMRI scan subject.
'''
import os
import pickle

class Subject():
	def __init__(self, sub_id, site_id, sex, age, data_dict={}, label_dict = {}):
		self._sub_id = sub_id
		self._site_id = site_id
		self._sex = sex
		self._age = age
		self._data_dict = data_dict
		self._label_dict = label_dict

	def _save_subject(self, save_folder):
		if not os.path.exists(save_folder):
			os.makedirs(save_folder)

		save_f = os.path.join(save_folder, f'{self._site_id}_{self._sub_id}_subject.pkl')
		with open(save_f, 'wb') as f:
			pickle.dump(self, f)

