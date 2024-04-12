import warnings

from langchain_core._api.deprecation import LangChainDeprecationWarning


def pre_precess():
    warnings.filterwarnings("ignore", category=LangChainDeprecationWarning)
