﻿using OpenQA.Selenium;
using OpenQA.Selenium.Internal;
using SeleniumWithPattern.Utils;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace SeleniumWithPattern.PageObjects
{
	public abstract class PageBase
	{
		private IWebDriver _webDriver;
		private IWebElement _relatedElement;

		public IWebDriver Driver
		{
			get => _webDriver ?? (_webDriver = ((IWrapsDriver)RelatedElement).WrappedDriver);
			set => _webDriver = value;
		}

		protected IWebElement RelatedElement
		{
			get => _relatedElement ?? (_relatedElement = Driver.FindElement("body"));
			set => _relatedElement = value;
		}

		public T Select<T>(string name, FindBy findBy = FindBy.CssSelector) where T : PageBase, new()
		{
			return new T
			{
				RelatedElement = RelatedElement.FindElement(name, findBy)
			};
		}

		public IReadOnlyCollection<T> SelectAll<T>(string name, FindBy findBy = FindBy.CssSelector) where T : PageBase, new()
		{
			var elements = RelatedElement.FindElements(name, findBy);
			return elements.Select(element => new T { RelatedElement = element }).ToArray();
		}

		public string FindText(string name, FindBy findBy = FindBy.CssSelector) => RelatedElement.FindElement(name, findBy)?.Text;
	}
}
