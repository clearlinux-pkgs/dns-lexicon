#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dns-lexicon
Version  : 3.3.8
Release  : 9
URL      : https://files.pythonhosted.org/packages/2b/ec/7d2bfaf13057f9e8c85da5706ecc24420d15d7b1932c9088445eeb240ba3/dns-lexicon-3.3.8.tar.gz
Source0  : https://files.pythonhosted.org/packages/2b/ec/7d2bfaf13057f9e8c85da5706ecc24420d15d7b1932c9088445eeb240ba3/dns-lexicon-3.3.8.tar.gz
Summary  : Manipulate DNS records on various DNS providers in a standardized/agnostic way
Group    : Development/Tools
License  : MIT
Requires: dns-lexicon-bin = %{version}-%{release}
Requires: dns-lexicon-license = %{version}-%{release}
Requires: dns-lexicon-python = %{version}-%{release}
Requires: dns-lexicon-python3 = %{version}-%{release}
Requires: PyYAML
Requires: cryptography
Requires: tldextract
BuildRequires : PyYAML
BuildRequires : buildreq-distutils3
BuildRequires : cryptography
BuildRequires : python-future
BuildRequires : testscenarios
BuildRequires : tldextract
BuildRequires : util-linux

%description
<p align="center">
<a href="https://github.com/AnalogJ/lexicon">
<img width="300" alt="lexicon_view" src="https://github.com/AnalogJ/lexicon/blob/master/logo.svg">
</a>
</p>

%package bin
Summary: bin components for the dns-lexicon package.
Group: Binaries
Requires: dns-lexicon-license = %{version}-%{release}

%description bin
bin components for the dns-lexicon package.


%package license
Summary: license components for the dns-lexicon package.
Group: Default

%description license
license components for the dns-lexicon package.


%package python
Summary: python components for the dns-lexicon package.
Group: Default
Requires: dns-lexicon-python3 = %{version}-%{release}

%description python
python components for the dns-lexicon package.


%package python3
Summary: python3 components for the dns-lexicon package.
Group: Default
Requires: python3-core

%description python3
python3 components for the dns-lexicon package.


%prep
%setup -q -n dns-lexicon-3.3.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1572185540
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/dns-lexicon
cp %{_builddir}/dns-lexicon-3.3.8/LICENSE %{buildroot}/usr/share/package-licenses/dns-lexicon/d7389b6482179505c25d9b209b006826fcb6b85c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/lexicon

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/dns-lexicon/d7389b6482179505c25d9b209b006826fcb6b85c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
