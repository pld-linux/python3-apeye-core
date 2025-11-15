Summary:	Core (offline) functionality for the apeye library
Summary(pl.UTF-8):	Podstawowa funkcjonalność (offline) biblioteki apeye
Name:		python3-apeye-core
Version:	1.1.5
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/apeye-core/
Source0:	https://files.pythonhosted.org/packages/source/a/apeye_core/apeye_core-%{version}.tar.gz
# Source0-md5:	16042e138de152aa471ccec4a4642577
URL:		https://github.com/domdfcoding/apeye-core
BuildRequires:	python3 >= 1:3.6.1
BuildRequires:	python3-build
BuildRequires:	python3-hatch-requirements-txt
BuildRequires:	python3-hatchling
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.6.1
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.6.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Core (offline) functionality for the apeye library.

%description -l pl.UTF-8
Podstawowa funkcjonalność (offline) biblioteki apeye.

%prep
%setup -q -n apeye_core-%{version}

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE README.rst
%dir %{py3_sitescriptdir}/apeye_core
%{py3_sitescriptdir}/apeye_core/*.py
%{py3_sitescriptdir}/apeye_core/__pycache__
%{py3_sitescriptdir}/apeye_core/public_suffix_list.dat
%{py3_sitescriptdir}/apeye_core/py.typed
%{py3_sitescriptdir}/apeye_core-%{version}.dist-info
