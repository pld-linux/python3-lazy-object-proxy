#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

Summary:	A fast and thorough lazy object proxy
Summary(pl.UTF-8):	Szybkie i gruntowne leniwe proxy obiektów
Name:		python3-lazy-object-proxy
Version:	1.11.0
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/lazy-object-proxy/
Source0:	https://files.pythonhosted.org/packages/source/l/lazy-object-proxy/lazy_object_proxy-%{version}.tar.gz
# Source0-md5:	0cac82f66458b23d6e5b0da11bce7663
URL:		https://github.com/ionelmc/python-lazy-object-proxy
BuildRequires:	python3-devel >= 1:3.9
BuildRequires:	python3-setuptools >= 1:64
BuildRequires:	python3-setuptools_scm >= 8
%if %{with tests}
#BuildRequires:	python3-django
#BuildRequires:	python3-hunter
BuildRequires:	python3-objproxies >= 0.9.4
BuildRequires:	python3-pytest
BuildRequires:	python3-pytest-benchmark
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with doc}
BuildRequires:	python3-furo
BuildRequires:	sphinx-pdg-3 >= 1.3
%endif
Requires:	python3-modules >= 1:3.9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A fast and thorough lazy object proxy.

%description -l pl.UTF-8
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
%setup -q -n lazy_object_proxy-%{version}

%build
%py3_build

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS="pytest_benchmark.plugin" \
PYTHONPATH=$(echo $(pwd)/build-3/lib.*) \
%{__python3} -m pytest -v tests
%endif

%if %{with doc}
PYTHONPATH=$(pwd)/src \
sphinx-build-3 -b html docs docs/_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/lazy_object_proxy/*.c

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS.rst CHANGELOG.rst LICENSE README.rst SECURITY.md
%dir %{py3_sitedir}/lazy_object_proxy
%{py3_sitedir}/lazy_object_proxy/*.py
%attr(755,root,root) %{py3_sitedir}/lazy_object_proxy/cext.cpython-*.so
%{py3_sitedir}/lazy_object_proxy/__pycache__
%{py3_sitedir}/lazy_object_proxy-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/{_static,*.html,*.js}
%endif
