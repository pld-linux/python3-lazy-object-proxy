#
# Conditional build:
%bcond_with	doc	# don't build doc
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define 	module	lazy-object-proxy
Summary:	A fast and thorough lazy object proxy
Name:		python-%{module}
Version:	1.4.1
Release:	1
License:	BSD
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/source/l/lazy-object-proxy/%{module}-%{version}.tar.gz
# Source0-md5:	0a904e9b6112c1337f404811e10cb53e
URL:		https://github.com/ionelmc/python-lazy-object-proxy
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-devel
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A fast and thorough lazy object proxy.

%package -n python3-%{module}
Summary:	A fast and thorough lazy object proxy
Group:		Libraries/Python
Requires:	python3-modules

%description -n python3-%{module}
A fast and thorough lazy object proxy.

%package apidocs
Summary:	%{module} API documentation
Summary(pl.UTF-8):	Dokumentacja API %{module}
Group:		Documentation

%description apidocs
API documentation for %{module}.

%description apidocs -l pl.UTF-8
Dokumentacja API %{module}.

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
sphinx-build -b html docs dist/docs
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
%doc *.rst
%dir %{py_sitedir}/lazy_object_proxy
%{py_sitedir}/lazy_object_proxy/*.py[co]
%attr(755,root,root) %{py_sitedir}/lazy_object_proxy/*.so
%{py_sitedir}/lazy_object_proxy-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc *.rst
%dir %{py3_sitedir}/lazy_object_proxy
%{py3_sitedir}/lazy_object_proxy/*.py
%attr(755,root,root) %{py3_sitedir}/lazy_object_proxy/*.so
%{py3_sitedir}/lazy_object_proxy/__pycache__
%{py3_sitedir}/lazy_object_proxy-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc dist/docs/html/*
%endif
