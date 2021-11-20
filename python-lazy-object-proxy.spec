#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	lazy-object-proxy
Summary:	A fast and thorough lazy object proxy
Summary(pl.UTF-8):	Szybkie i gruntowne leniwe proxy obiektów
Name:		python-%{module}
Version:	1.4.3
Release:	3
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/lazy-object-proxy/
Source0:	https://files.pythonhosted.org/packages/source/l/lazy-object-proxy/%{module}-%{version}.tar.gz
# Source0-md5:	5c64c06affcd2a7c6ddc848af4280cca
URL:		https://github.com/ionelmc/python-lazy-object-proxy
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-devel >= 1:2.7
BuildRequires:	python-setuptools >= 30.3.0
BuildRequires:	python-setuptools_scm >= 3.3.1
%endif
%if %{with python3}
BuildRequires:	python3-devel >= 1:3.4
BuildRequires:	python3-setuptools >= 30.3.0
BuildRequires:	python3-setuptools_scm >= 3.3.1
%endif
%if %{with doc}
BuildRequires:	python3-sphinx_py3doc_enhanced_theme
BuildRequires:	sphinx-pdg-3 >= 1.3
%endif
Requires:	python-modules >= 1:2.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A fast and thorough lazy object proxy.

%description -l pl.UTF-8
Szybkie i gruntowne leniwe proxy obiektów.

%package -n python3-%{module}
Summary:	A fast and thorough lazy object proxy
Summary(pl.UTF-8):	Szybkie i gruntowne leniwe proxy obiektów
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-%{module}
A fast and thorough lazy object proxy.

%description -n python3-%{module} -l pl.UTF-8
Szybkie i gruntowne leniwe proxy obiektów.

%package apidocs
Summary:	API documentation for lazy_object_proxy module
Summary(pl.UTF-8):	Dokumentacja API modułu lazy_object_proxy
Group:		Documentation

%description apidocs
API documentation for lazy_object_proxy module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu lazy_object_proxy.

%prep
%setup -q -n %{module}-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%if %{with doc}
sphinx-build-3 -b html docs docs/_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS.rst CHANGELOG.rst LICENSE README.rst
%dir %{py_sitedir}/lazy_object_proxy
%{py_sitedir}/lazy_object_proxy/*.py[co]
%attr(755,root,root) %{py_sitedir}/lazy_object_proxy/cext.so
%{py_sitedir}/lazy_object_proxy-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc AUTHORS.rst CHANGELOG.rst LICENSE README.rst
%dir %{py3_sitedir}/lazy_object_proxy
%{py3_sitedir}/lazy_object_proxy/*.py
%attr(755,root,root) %{py3_sitedir}/lazy_object_proxy/cext.cpython-*.so
%{py3_sitedir}/lazy_object_proxy/__pycache__
%{py3_sitedir}/lazy_object_proxy-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/{_static,*.html,*.js}
%endif
